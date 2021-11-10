frappe.ui.form.on('Purchase Order', {
	refresh(frm) {
		frm.add_custom_button(__("Auto Requisition Form"), function () {
			var d = new frappe.ui.Dialog({
				title: "Fetch ARF Items",
				fields: [
					{
						label: __("ARF Name"),
						fieldname: "arfname",
						fieldtype: "Link",
						options: "Auto Requisition Form"
					}
				],
				primary_action_label: __("Fetch ARF Items"),
				primary_action: function (values) {
					frappe.call({
						method: 'khutuut_addons.arf.fetch_arf_items',
						args: { 'arf_name': values.arfname },
						callback: function (r) {
							// preparations
							d.hide();
							frm.clear_table("items");
							refresh_field("items");
							
							var arf_items = r.message;

							for (var i = 0; i < arf_items.length; i++) {
								console.log(arf_items[i])
								var row = frm.add_child("items");
								row.item_code = arf_items[i].item_code;
								row.item_name = arf_items[i].item_name;
								row.description = arf_items[i].description;
								row.image_view = arf_items[i].image;
								row.qty = arf_items[i].qty
								row.stock_qty = arf_items[i].stock_qty;
								row.uom = arf_items[i].uom;
								row.stock_uom = arf_items[i].stock_uom;
								row.price_list_rate = arf_items[i].price_list_rate;
								row.last_purchase_rate = arf_items[i].last_purchase_rate;
								row.rate = arf_items[i].rate;
								row.base_rate = arf_items[i].base_rate;
								row.stock_uom_rate = arf_items[i].stock_uom_rate;
								row.amount = arf_items[i].amount;
								row.net_rate = arf_items[i].net_rate;
								row.net_amount = arf_items[i].net_amount;
								row.warehouse = arf_items[i].warehouse;
								row.against_blanket_order = arf_items[i].against_blanket_order;
								row.actual_qty = arf_items[i].actual_qty;
								row.company_total_stock = arf_items[i].company_total_stock;
								row.expense_acount = arf_items[i].expense_acount;
								row.manufacturer = arf_items[i].manufacturer;
								row.manufacturer_part_no = arf_items[i].manufacturer_part_no;
								row.weight_per_unit = arf_items[i].weight_per_unit;
								row.supplier = arf_items[i].supplier;
								row.conversion_factor = arf_items[i].conversion_factor;

							}
							frm.scroll_to_field("items");
							refresh_field("items");
						}
					})
				}
			})
			d.show();

		}, [__("Get Items From")]);
	}
})