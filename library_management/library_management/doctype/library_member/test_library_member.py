# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
import unittest

class TestLibraryMember(unittest.TestCase):
	def test_member_creation(self):
		"""Test basic member creation"""
		member = frappe.get_doc({
			"doctype": "Library Member",
			"first_name": "John",
			"last_name": "Doe",
			"email_id": "john.doe@example.com",
			"phone_number": "1234567890"
		})
		member.insert()

		self.assertEqual(member.full_name, "John Doe")
		self.assertEqual(member.email_id, "john.doe@example.com")

		# Cleanup
		member.delete()

	def test_full_name_generation(self):
		"""Test automatic full name generation"""
		member = frappe.get_doc({
			"doctype": "Library Member",
			"first_name": "Jane",
			"email_id": "jane@example.com"
		})
		member.insert()

		self.assertEqual(member.full_name, "Jane")

		# Cleanup
		member.delete()
