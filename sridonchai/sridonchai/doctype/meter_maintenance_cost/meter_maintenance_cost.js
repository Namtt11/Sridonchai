// Copyright (c) 2024, university of phayao and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Meter Maintenance Cost", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Meter Maintenance Cost", "onload", function(frm){
    frm.set_query("user", function(){
        return {
            filters: {
                "ignore_user_type": 1
            }
        }
    });
});
