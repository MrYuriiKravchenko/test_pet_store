def test_post_user_wishlist(post_createwishlist_endp,random_id, random_string, random_password, radom_email, random_phone):
    post_createwishlist_endp.post_createwishlist(random_id, random_string, random_password, radom_email, random_phone)
    post_createwishlist_endp.check_response_status_is_ok()

