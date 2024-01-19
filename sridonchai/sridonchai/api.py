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

@frappe.whitelist(allow_guest=True)
def get_overdue_house() :
    request = frappe.form_dict


    

    result = frappe.db.sql(
        f"""
        select tabHouse.name,owner_name,house_number ,`tabWater Usage`.paid, `tabWater Usage`.total_price,`tabWater Usage`.current_meter_unit,sum(`tabWater Usage`.total_price) as overdue from tabHouse
        left join `tabWater Usage` on tabHouse.name = `tabWater Usage`.house and `tabWater Usage`.paid = 0
        group by tabHouse.name
        """,
        as_dict=True
    )


            
            

    return result


@frappe.whitelist(allow_guest=True)
def get_info_house() :
    request = frappe.form_dict


    
    #x
    result = frappe.db.sql(
        f"""
        select `tabHouse`.owner_name, `tabHouse`.house_number from `tabHouse`
        """,

        as_dict=True
    )
    #y
    result2 = frappe.db.sql(
        f"""
        select `tabWater Usage`.month ,`tabWater Usage`.total_unit,`tabWater Usage`.total_price ,`tabHouse`.owner_name,`tabHouse`.house_number from tabHouse
        left join `tabWater Usage` on tabHouse.name = `tabWater Usage`.house
        """,
        
        as_dict=True
    )
    def get_name_month(text):
        if text=="01":
            return ("มกราคม")
        elif text=="02":
            return ("กุมภาพันธ์")
        elif text=="03":
            return ("มีนาคม")
        
    for i in result:
        b=[j for j in result2 if j['owner_name']==i['owner_name'] ]
        i['Usages']=b
    for i in result:
        for j in i['Usages']:
            text=j['month']
            month=text.split("-")[1]
            month=get_name_month(month)
            j['month']=month

    return result



