def test_store_order_id(create_order_for_test, get_store_order_id_endp, random_id_order, random_id, current_ship_date):
    order_id = create_order_for_test.order_id
    get_store_order_id_endp.get_order_id(order_id)
    get_store_order_id_endp.check_response_status_is_ok()
    get_store_order_id_endp.check_that_the_id_match(order_id)
    get_store_order_id_endp.check_petId_same_as_sent(random_id)
    get_store_order_id_endp.check_quantity_correct(random_id)
    get_store_order_id_endp.check_ship_date_for_order(current_ship_date)
    get_store_order_id_endp.check_status_place_order()
    get_store_order_id_endp.check_complete_order()
