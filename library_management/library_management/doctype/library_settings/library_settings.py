# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibrarySettings(Document):
	def validate(self):
		"""Validation method for Library Settings DocType"""
		if self.loan_period and self.loan_period < 1:
			frappe.throw("Loan period must be at least 1 day")

		if self.max_books and self.max_books < 1:
			frappe.throw("Maximum books per member must be at least 1")

		if self.fine_per_day and self.fine_per_day < 0:
			frappe.throw("Fine per day cannot be negative")
