# Copyright (c) 2020, Frappe Technologies and contributors
# License: MIT. See LICENSE

# import frappe
from frappe.model.document import Document


class DocTypeLayoutField(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		fieldname: DF.Literal
		label: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass