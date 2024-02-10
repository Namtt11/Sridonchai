# Copyright (c) 2024, university of phayao and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MeterMaintenanceCost(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date | None
		date_recieve: DF.Date | None
		house: DF.Link | None
		meter_cost_paid: DF.Data | None
		month: DF.Link | None
		user: DF.Link | None
	# end: auto-generated types

	pass
