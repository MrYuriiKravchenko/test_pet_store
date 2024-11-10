def test_put_user_username(put_user_endp, create_user_for_test, random_id, random_string, random_password, radom_email, random_phone):
    username = create_user_for_test.username
    put_user_endp.put_user(username, random_id, random_string, random_password, radom_email, random_phone)
    put_user_endp.check_response_status_is_ok()
