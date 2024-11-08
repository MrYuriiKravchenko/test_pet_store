def test_delete_store_order(create_order_for_test, delete_oreder_is_endp):
    order_id = create_order_for_test.order_id
    delete_oreder_is_endp.delete_order(order_id)
    delete_oreder_is_endp.check_response_status_is_ok()
