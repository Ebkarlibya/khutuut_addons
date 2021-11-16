import frappe
from erpnext.stock.get_item_details import get_item_details
from frappe.utils import get_url_to_form, get_url_to_list

def on_submit(doc, method):

    for row in doc.auto:    
        d = frappe.get_doc({
            "doctype": "Item",
            "disabled": False,
            "item_name": row.item_name,
            "item_code": f"itm-{row.item_name.lower()}",
            "item_group": row.item_group,
            "created_by_arf": doc.name,
            "stock_uom": "Nos",
            "is_stock_item": True,
            "include_item_in_manufacturing": False,
            "brand": row.brand,
            "description": row.description,
            "engine_type": row.engine_type,
            "body_color": row.body_color,
            "interior_color": row.interior_color,
            "indoor_seat_type": row.indoor_seat_type,
            "tire_size": row.tire_size,
            "external_cameras": row.external_cameras,
            "camera_type": row.camera_type,
            "steering_wheel_control": row.steering_wheel_control,
            "number_of_airbags": row.number_of_airbags,
            "number_of_seats": row.number_of_seats,
            "keys_type": row.keys_type,
            "external_sensors": row.external_sensors,
            "outdoor_lights": row.outdoor_lights,
            "bluetooth": row.bluetooth,
            "sunroof": row.sunroof,
            "indoor_screen": row.indoor_screen,
            "touch_screen": row.touch_screen,
            "instrument_cluster": row.instrument_cluster
        })

        d.save()
    frappe.msgprint(frappe._(f"New ARF Items Created!, <a href='{get_url_to_list('Item')}'>View Items Now</a>"))

def on_cancel(doc, method):
    linked_items = frappe.get_all("Item", filters={"created_by_arf": doc.name})

    if len(linked_items) > 0:
        items_links_list = ""
        for lItem in linked_items:
            items_links_list += f"<a href='{get_url_to_form('Item', lItem.name)}'>{lItem.name}</a>, "
            
        msg = f"Cannot Cancle, ARF {doc.name} is linked with the items: {items_links_list}"
        frappe.throw(msg)

def on_trash(doc, method):
    pass



@frappe.whitelist()
def fetch_arf_items(arf_name):
    arf_items = frappe.get_all("Item", fields=["item_code"], filters={"created_by_arf": arf_name})
    arf_details = []
    
    for arf_item in arf_items:
        arf_details.append(
            get_item_details({
                "item_code": arf_item.item_code,
                "company": "Khutu Almutawasit Co.",
                "conversion_rate": 1,
                "doctype": "Purchase Order"
            })
        )

    return arf_details
