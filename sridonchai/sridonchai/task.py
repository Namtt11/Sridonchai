import frappe
def insert_meter_cost():
    date=frappe.utils.today()
    month=date[0:7]
#get a single doctype
    doc = frappe.get_doc('Sridonchai config')
    doc.meter_maintenance_cost
    result = frappe.db.sql(
            f"""
            select `tabHouse`.name from `tabHouse`
            """,

            as_dict=True
    )
    result2= frappe.db.sql(
    
            f"""
            select house from`tabMeter Maintenance Cost`
            left join `tabMonthly`on `tabMonthly`.name=`tabMeter Maintenance Cost`.month
            where  `tabMeter Maintenance Cost`.month is not null and LPAD(month(`tabMeter Maintenance Cost`.transaction_date), 2, '0')=`tabMonthly`.month and year(transaction_date)=`tabMonthly`.year


         
            """,

            as_dict=True
    )
    b=[j.house for j in result2]
    for i in result:
    
    
        if i.name not in b:
            document_insert= frappe.get_doc({
                'doctype': 'Meter Maintenance Cost',
                'cost_paid': 5,
                'house':i.name,
                'transaction_date':date,
                'month':month
            
    })  
        
            document_insert.insert(ignore_permissions=True)
            frappe.db.commit()
    return document_insert
    