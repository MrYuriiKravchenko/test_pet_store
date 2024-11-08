def test_get_iventory(get_inventory_endp):
    get_inventory_endp.get_inventory()
    get_inventory_endp.check_response_status_is_ok()
    get_inventory_endp.check_response_contains_dict()