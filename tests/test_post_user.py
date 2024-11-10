def test_post_user_petstore(post_user_endp, random_id, random_string, random_password, random_phone, radom_email):
    post_user_endp.post_user(random_id, random_string, random_password, random_phone, radom_email)
    post_user_endp.check_response_status_is_ok()