# Copyright (c) 2023, university of phayao and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class House(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		house_number: DF.Data | None
		owner_name: DF.Data | None
	# end: auto-generated types

	pass
