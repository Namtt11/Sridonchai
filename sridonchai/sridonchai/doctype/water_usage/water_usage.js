// Copyright (c) 2023, university of phayao and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Water Usage", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Water Usage", "onload", function(frm){
    frm.set_query("user", function(){
        return {
            filters: {
                "ignore_user_type": 1
            }
        }
    });
});
