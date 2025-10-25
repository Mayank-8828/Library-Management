# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from frappe.utils import add_days, today


class LibraryMembership(Document):
	def validate(self):
		"""Validation method for Library Membership DocType"""
		if self.from_date and self.to_date:
			if self.from_date > self.to_date:
				frappe.throw("From Date cannot be greater than To Date")

	def before_save(self):
		"""Calculate to_date based on loan period from Library Settings"""
		if self.from_date and not self.to_date:
			loan_period = frappe.db.get_single_value("Library Settings", "loan_period") or 30
			self.to_date = add_days(self.from_date, loan_period)

	def before_submit(self):
		"""Check if there's already an active membership for this member"""
		# Check for overlapping memberships
		existing = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				"to_date": [">", self.from_date],
				"name": ["!=", self.name]
			}
		)

		if existing:
			frappe.throw("There is already an active membership for this member")

	def on_submit(self):
		"""Actions after successful submission"""
		frappe.msgprint(f"Membership created successfully for {self.full_name}")

	def get_remaining_days(self):
		"""Get remaining days for membership"""
		from frappe.utils import date_diff

		if self.to_date:
			remaining = date_diff(self.to_date, today())
			return max(0, remaining)
		return 0
