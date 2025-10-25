from frappe import _

def get_data():
	return [
		{
			"module_name": "Library Management",
			"category": "Modules",
			"label": _("Library Management"),
			"color": "#FF6B35",
			"reverse": 1,
			"icon": "octicon octicon-book",
			"type": "module",
			"description": "Library Management System for managing books, members, and transactions"
		}
	]
