# Copyright (c) 2023, university of phayao and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Monthly(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		month: DF.Literal["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
		year: DF.Data | None
	# end: auto-generated types

	pass
