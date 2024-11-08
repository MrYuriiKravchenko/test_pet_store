def test_order_store(post_order_endp, random_id, random_id_order, current_ship_date):
    post_order_endp.post_order(random_id, random_id_order, current_ship_date)
    post_order_endp.check_response_status_is_ok()
    post_order_endp.check_that_the_id_match(random_id_order)
    post_order_endp.check_petId_same_as_sent(random_id)
    post_order_endp.check_quantity_correct(random_id)
    post_order_endp.check_ship_date_for_order(current_ship_date)
    post_order_endp.check_status_place_order()
    post_order_endp.check_complete_order()
