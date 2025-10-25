# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from frappe.utils import today, add_days


class LibraryTransaction(Document):
	def validate(self):
		"""Validation method for Library Transaction DocType"""
		if self.type == "Issue":
			self.validate_membership()
			self.validate_maximum_limit()

		# Set due date for issued books
		if self.type == "Issue" and self.date and not self.due_date:
			loan_period = frappe.db.get_single_value("Library Settings", "loan_period") or 14
			self.due_date = add_days(self.date, loan_period)

	def before_submit(self):
		"""Perform validations before submit"""
		if self.type == "Issue":
			self.validate_issue()
		elif self.type == "Return":
			self.validate_return()

	def on_submit(self):
		"""Update book status after successful submission"""
		if self.type == "Issue":
			# Set book status to Issued
			book = frappe.get_doc("Book", self.book)
			book.status = "Issued"
			book.save()
			frappe.msgprint(f"Book '{self.book_title}' has been issued to {self.member_name}")

		elif self.type == "Return":
			# Set book status to Available
			book = frappe.get_doc("Book", self.book)
			book.status = "Available"
			book.save()
			frappe.msgprint(f"Book '{self.book_title}' has been returned by {self.member_name}")

	def validate_issue(self):
		"""Validate book issue transaction"""
		book = frappe.get_doc("Book", self.book)

		# Check if book is already issued
		if book.status == "Issued":
			frappe.throw(f"Book '{book.title}' is already issued to another member")

	def validate_return(self):
		"""Validate book return transaction"""
		book = frappe.get_doc("Book", self.book)

		# Check if book is available (not issued)
		if book.status == "Available":
			frappe.throw(f"Book '{book.title}' is not currently issued and cannot be returned")

		# Check if this member has actually issued this book
		issued_transaction = frappe.db.exists(
			"Library Transaction",
			{
				"library_member": self.library_member,
				"book": self.book,
				"type": "Issue",
				"docstatus": 1
			}
		)

		if not issued_transaction:
			frappe.throw(f"Book '{book.title}' was not issued to this member")

	def validate_membership(self):
		"""Check if member has valid active membership"""
		valid_membership = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				"from_date": ["<=", self.date],
				"to_date": [">=", self.date]
			}
		)

		if not valid_membership:
			frappe.throw(f"Member {self.member_name} does not have a valid active membership")

	def validate_maximum_limit(self):
		"""Check if member has reached maximum book limit"""
		max_books = frappe.db.get_single_value("Library Settings", "max_books") or 3

		# Count currently issued books by this member
		issued_count = frappe.db.count(
			"Library Transaction",
			{
				"library_member": self.library_member,
				"type": "Issue",
				"docstatus": 1
			}
		)

		# Count returns to get net issued books
		returned_count = frappe.db.count(
			"Library Transaction",
			{
				"library_member": self.library_member,
				"type": "Return",
				"docstatus": 1
			}
		)

		net_issued = issued_count - returned_count

		if net_issued >= max_books:
			frappe.throw(f"Member {self.member_name} has reached the maximum limit of {max_books} books")

	def get_overdue_days(self):
		"""Calculate overdue days for issued books"""
		if self.type == "Issue" and self.due_date:
			from frappe.utils import date_diff
			overdue = date_diff(today(), self.due_date)
			return max(0, overdue)
		return 0
