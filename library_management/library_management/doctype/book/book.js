// Copyright (c) 2025, Your Name and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book', {
	refresh: function(frm) {
		// Add custom buttons or logic here
		if (frm.doc.status === 'Available') {
			frm.add_custom_button(__('Issue Book'), function() {
				frappe.new_doc('Library Transaction', {
					book: frm.doc.name,
					type: 'Issue'
				});
			});
		}
	}
});
