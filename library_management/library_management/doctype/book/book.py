# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Book(Document):
	def validate(self):
		"""Validation method for Book DocType"""
		if not self.title:
			frappe.throw("Book title is mandatory")

		# Ensure ISBN is unique if provided
		if self.isbn:
			existing = frappe.db.exists("Book", {"isbn": self.isbn, "name": ["!=", self.name]})
			if existing:
				frappe.throw(f"Book with ISBN {self.isbn} already exists")

	def before_save(self):
		"""Method called before saving the document"""
		# Auto-set status to Available if not set
		if not self.status:
			self.status = "Available"
