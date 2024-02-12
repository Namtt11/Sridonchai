# Copyright (c) 2024, university of phayao and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Sridonchaiconfig(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		meter_maintenance_cost: DF.Data | None
		unit_per_month: DF.Data | None
	# end: auto-generated types

	pass
