// Copyright (c) 2025, Your Name and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	refresh: function(frm) {
		// Set color indicator based on transaction type
		if (frm.doc.type === 'Issue') {
			frm.dashboard.add_indicator(__('Issue Transaction'), 'orange');
		} else if (frm.doc.type === 'Return') {
			frm.dashboard.add_indicator(__('Return Transaction'), 'blue');
		}

		// Show due date warning for overdue books
		if (frm.doc.type === 'Issue' && frm.doc.due_date && frm.doc.docstatus === 1) {
			let today = frappe.datetime.get_today();
			if (frm.doc.due_date < today) {
				let overdue_days = frappe.datetime.get_diff(today, frm.doc.due_date);
				frm.dashboard.add_indicator(__('Overdue by {0} days', [overdue_days]), 'red');
			}
		}
	},

	type: function(frm) {
		// Clear book selection when type changes
		frm.set_value('book', '');

		// Show/hide due date based on type
		frm.toggle_display('due_date', frm.doc.type === 'Issue');
	},

	book: function(frm) {
		// Auto-fetch book title
		if (frm.doc.book) {
			frappe.db.get_value('Book', frm.doc.book, ['title', 'status'])
				.then(r => {
					if (r.message) {
						frm.set_value('book_title', r.message.title);

						// Validate book availability for issue
						if (frm.doc.type === 'Issue' && r.message.status === 'Issued') {
							frappe.msgprint(__('This book is already issued to another member'));
							frm.set_value('book', '');
						}
					}
				});
		}
	},

	library_member: function(frm) {
		// Auto-fetch member name
		if (frm.doc.library_member) {
			frappe.db.get_value('Library Member', frm.doc.library_member, 'full_name')
				.then(r => {
					if (r.message) {
						frm.set_value('member_name', r.message.full_name);
					}
				});
		}
	},

	date: function(frm) {
		// Auto-calculate due date for issue transactions
		if (frm.doc.type === 'Issue' && frm.doc.date && !frm.doc.due_date) {
			frappe.db.get_single_value('Library Settings', 'loan_period')
				.then(loan_period => {
					if (loan_period) {
						let due_date = frappe.datetime.add_days(frm.doc.date, loan_period);
						frm.set_value('due_date', due_date);
					}
				});
		}
	}
});
