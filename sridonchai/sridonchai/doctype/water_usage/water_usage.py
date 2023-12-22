# Copyright (c) 2023, university of phayao and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class WaterUsage(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from sridonchai.sridonchai.doctype.housemanaged.housemanaged import HouseManaged

		current_meter_unit: DF.Int
		date: DF.Date | None
		house: DF.Table[HouseManaged]
		last_meter_unit: DF.Int
		month: DF.Literal["Monthly"]
		total_price: DF.Int
		total_unit: DF.Int
		user: DF.Table[HouseManaged]
	# end: auto-generated types

	pass
