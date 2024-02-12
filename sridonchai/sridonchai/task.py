import frappe
def x():
    doc = frappe.get_doc('Sridonchai config')
    doc.meter_maintenance_cost
    result = frappe.db.sql(
            f"""
            select `tabHouse`.owner_name, `tabHouse`.house_number from `tabHouse`
            where active= 1
            """,

            as_dict=True
        )
    document = frappe.get_doc({
        'doctype': 'Meter Maintenance Cost',
        'cost_paid': '5',
        'house':'143 - อ.ทวีศักดิ์  รักษาศรี',
        'month':'2024-01'
    })
    document.insert()
