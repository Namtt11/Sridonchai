import frappe

@frappe.whitelist(allow_guest=False)
def get_house_status_by_month() :
    request = frappe.form_dict
    current_user=frappe.session.user

    month = request['month']

    result = frappe.db.sql(
        f"""
            SELECT tabHouse.name,owner_name,house_number ,`tabWater Usage`.month,`tabWater Usage`.date_recieve,`tabWater Usage`.total_price FROM tabHouseManagement
            join `tabHouseManaged` on 	`tabHouseManaged`.parent = tabHouseManagement.name
            left join `tabHouse` On `tabHouse`.name= tabHouseManaged.house
            left join `tabWater Usage` on tabHouse.name = `tabWater Usage`.house and `tabWater Usage`.month= '{month}'
        
            where tabHouseManagement.user = '{current_user}'
    
        """
       ,


        as_dict=True
    )
   
    
    


    for i in result :
        if i.date_recieve != None :
            i['status'] = "เก็บเงินแล้ว"
        elif i.total_price !=None:
             i['status'] = "จดมิเตอร์แล้ว"
        elif i.total_price == None :
            i['status'] = "ยังไม่ได้ดำเนินการ"
            


@frappe.whitelist(allow_guest=True)
def get_overdue_house() :
    request = frappe.form_dict


    

    result = frappe.db.sql(
        f"""
        select tabHouse.name,owner_name,house_number ,`tabWater Usage`.paid, `tabWater Usage`.total_price,`tabWater Usage`.current_meter_unit,sum(`tabWater Usage`.total_price) as overdue from tabHouse
        left join `tabWater Usage` on tabHouse.name = `tabWater Usage`.house and `tabWater Usage`.date_recieve is null
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

@frappe.whitelist(allow_guest=False)
def get_current_user_info() :
    request = frappe.form_dict
    current_user=frappe.session.user
    return frappe.db.get_list('User',
        filters={
            'name': current_user
        },
        fields=['email', 'first_name','last_name'],
        as_list=True
    )




