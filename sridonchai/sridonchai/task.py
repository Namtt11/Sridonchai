import frappe
def insert_meter_cost():
    date=frappe.utils.today()
    month=date[0:7]
    #get a single doctype
    doc = frappe.get_doc('Sridonchai config')
    doc.meter_maintenance_cost
    result = frappe.db.sql(
            f"""
            select `tabHouse`.owner_name, `tabHouse`.house_number,`tabHouse`.name from `tabHouse`
            where active= 1
            """,

            as_dict=True
        )

    for i in result:
        document_insert= frappe.get_doc({
            'doctype': 'Meter Maintenance Cost',
            'cost_paid': 5,
            'house':i.name,
            'transaction_date':date,
            'month':month,
        
            
        
        })
        document_insert.insert()
    return document_insert
    