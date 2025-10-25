// Copyright (c) 2025, Your Name and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh: function(frm) {
		// Show membership status
		if (frm.doc.docstatus === 1) {
			frm.dashboard.add_indicator(__('Active Membership'), 'green');
		}
	},

	library_member: function(frm) {
		// Auto-fetch member details
		if (frm.doc.library_member) {
			frappe.db.get_value('Library Member', frm.doc.library_member, 'full_name')
				.then(r => {
					if (r.message) {
						frm.set_value('full_name', r.message.full_name);
					}
				});
		}
	},

	from_date: function(frm) {
		// Auto-calculate to_date based on loan period
		if (frm.doc.from_date && !frm.doc.to_date) {
			frappe.db.get_single_value('Library Settings', 'loan_period')
				.then(loan_period => {
					if (loan_period) {
						let to_date = frappe.datetime.add_days(frm.doc.from_date, loan_period);
						frm.set_value('to_date', to_date);
					}
				});
		}
	}
});
