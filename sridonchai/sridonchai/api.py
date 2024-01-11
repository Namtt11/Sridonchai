import frappe

@frappe.whitelist(allow_guest=True)
def get_house_status_by_month() :
    request = frappe.form_dict


    month = request['month']

    result = frappe.db.sql(
        f"""
        select tabHouse.name,owner_name,house_number ,`tabWater Usage`.month,`tabWater Usage`.paid  from tabHouse
        left join `tabWater Usage` on tabHouse.name = `tabWater Usage`.house and `tabWater Usage`.month= '{month}'
        """,
        as_dict=True
    )


    for i in result :
        if i.paid == 1 :
            i['status'] = "เก็บเงินแล้ว"
        elif i.paid == 0 :
            i['status'] = "จดมิเตอร์แล้ว"
        else :
            i['status'] = "ยังไม่ได้ดำเนินการ"
            
            

    return result