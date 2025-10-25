# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
import unittest

class TestBook(unittest.TestCase):
	def test_book_creation(self):
		"""Test basic book creation"""
		book = frappe.get_doc({
			"doctype": "Book",
			"title": "Test Book",
			"author": "Test Author",
			"isbn": "1234567890",
			"status": "Available"
		})
		book.insert()

		self.assertEqual(book.title, "Test Book")
		self.assertEqual(book.status, "Available")

		# Cleanup
		book.delete()

	def test_isbn_uniqueness(self):
		"""Test ISBN uniqueness validation"""
		# Create first book
		book1 = frappe.get_doc({
			"doctype": "Book",
			"title": "Test Book 1",
			"author": "Test Author",
			"isbn": "1234567890",
			"status": "Available"
		})
		book1.insert()

		# Try to create second book with same ISBN
		book2 = frappe.get_doc({
			"doctype": "Book",
			"title": "Test Book 2",
			"author": "Test Author",
			"isbn": "1234567890",
			"status": "Available"
		})

		with self.assertRaises(frappe.ValidationError):
			book2.insert()

		# Cleanup
		book1.delete()
