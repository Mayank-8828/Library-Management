# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	def validate(self):
		"""Validation method for Library Member DocType"""
		# Auto-generate full name
		self.full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()

		if not self.full_name:
			frappe.throw("First Name is required")

		# Validate email format
		if self.email_id and "@" not in self.email_id:
			frappe.throw("Please enter a valid email address")

	def before_save(self):
		"""Method called before saving the document"""
		# Ensure full name is properly set
		if self.first_name:
			self.full_name = f"{self.first_name} {self.last_name or ''}".strip()

	def get_active_membership(self):
		"""Get active membership for this member"""
		from frappe.utils import today

		active_membership = frappe.db.get_value(
			"Library Membership",
			{
				"library_member": self.name,
				"from_date": ["<=", today()],
				"to_date": [">=", today()],
				"docstatus": 1
			},
			["name", "to_date"]
		)

		return active_membership
