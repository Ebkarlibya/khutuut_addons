from . import __version__ as app_version

app_name = "khutuut_addons"
app_title = "Khutuut Addons"
app_publisher = "Ebkar "
app_description = "extras"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@ebkar.ly"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/khutuut_addons/css/khutuut_addons.css"
# app_include_js = "/assets/khutuut_addons/js/khutuut_addons.js"

# include js, css files in header of web template
# web_include_css = "/assets/khutuut_addons/css/khutuut_addons.css"
# web_include_js = "/assets/khutuut_addons/js/khutuut_addons.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "khutuut_addons/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Purchase Order" : "scripts/po_arf.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "khutuut_addons.install.before_install"
# after_install = "khutuut_addons.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "khutuut_addons.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Auto Requisition Form": {
		"on_submit": "khutuut_addons.arf.on_submit",
		"on_cancel": "khutuut_addons.arf.on_cancel",
		"on_trash": "khutuut_addons.arf.on_trash"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"khutuut_addons.tasks.all"
# 	],
# 	"daily": [
# 		"khutuut_addons.tasks.daily"
# 	],
# 	"hourly": [
# 		"khutuut_addons.tasks.hourly"
# 	],
# 	"weekly": [
# 		"khutuut_addons.tasks.weekly"
# 	]
# 	"monthly": [
# 		"khutuut_addons.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "khutuut_addons.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "khutuut_addons.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "khutuut_addons.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"khutuut_addons.auth.validate"
# ]

fixtures = [
	{
		"doctype": "Custom Field",
		"filters": [
			["dt", "=", "Item"]
		]
	},
	{
		"doctype": "Workspace",
		"filters": [
			["name", "in", ("Buying")]
		]
	}
]