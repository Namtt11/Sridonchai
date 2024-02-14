import frappe

@frappe.whitelist(allow_guest=False)
#แสดงสถานะของบ้านที่เจ้าหน้าที่ที่ล็อกอินจัดการ
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
            

    return result

@frappe.whitelist(allow_guest=False)
def get_overdue_house() :
    request = frappe.form_dict
    current_user=frappe.session.user

    

    result = frappe.db.sql(
        f"""
        SELECT tabHouse.owner_name,house_number , `tabWater Usage`.total_price,`tabWater Usage`.current_meter_unit,sum(`tabWater Usage`.total_price) as overdue FROM tabHouseManagement
        join `tabHouseManaged` on 	`tabHouseManaged`.parent = tabHouseManagement.name
        left join `tabHouse` On `tabHouse`.name= tabHouseManaged.house
        left join `tabWater Usage` on tabHouse.name = `tabWater Usage`.house and `tabWater Usage`.date_recieve is not null
        where tabHouseManagement.user = '{current_user}' 
        group by tabHouse.name
      
        """,
        as_dict=True
    )


            
            

    return result

#แสดงข้อมูลบ้านและข้อมูลการใช้น้ำ หน่วยน้ำ ค่าน้ำ
@frappe.whitelist(allow_guest=True)
def get_info_house() :
    request = frappe.form_dict
    name=request["name"]

    
    #x
    result = frappe.db.sql(
        f"""
        select `tabHouse`.owner_name, `tabHouse`.house_number,`tabHouse`.name from `tabHouse`
        where `tabHouse`.name='{name}'
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
  
        
    for i in result:
        b=[j for j in result2 if j['owner_name']==i['owner_name'] ]
        i['Usages']=b
    

    return result[0] if len(result)>0 else None

@frappe.whitelist(allow_guest=False)
def get_current_user_info() :
    request = frappe.form_dict
    current_user=frappe.session.user
    return frappe.db.get_list('User',
        filters={
            'name': current_user
        },
        fields=['email', 'first_name','last_name'],
    )[0]




