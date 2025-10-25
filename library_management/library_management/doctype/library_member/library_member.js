// Copyright (c) 2025, Your Name and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Member', {
	refresh: function(frm) {
		// Add custom buttons
		frm.add_custom_button(__('Create Membership'), function() {
			frappe.new_doc('Library Membership', {
				library_member: frm.doc.name,
				full_name: frm.doc.full_name
			});
		});

		frm.add_custom_button(__('Create Transaction'), function() {
			frappe.new_doc('Library Transaction', {
				library_member: frm.doc.name
			});
		});
	},

	first_name: function(frm) {
		// Auto-generate full name when first name changes
		if (frm.doc.first_name) {
			frm.set_value('full_name', frm.doc.first_name + ' ' + (frm.doc.last_name || ''));
		}
	},

	last_name: function(frm) {
		// Auto-generate full name when last name changes
		if (frm.doc.first_name) {
			frm.set_value('full_name', frm.doc.first_name + ' ' + (frm.doc.last_name || ''));
		}
	}
});
