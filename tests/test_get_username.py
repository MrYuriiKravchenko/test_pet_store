def test_get_user_username(get_username_endp, create_user_for_test, random_id, random_string, random_password, radom_email, random_phone):
    username = create_user_for_test.username
    get_username_endp.get_username(username)
    get_username_endp.check_response_status_is_ok()
    get_username_endp.check_id_user(random_id)
    get_username_endp.check_username(random_string)
    get_username_endp.check_firsrt_name_user(random_string)
    get_username_endp.check_firsrt_name_user(random_string)
    get_username_endp.check_email_user(radom_email)
    get_username_endp.check_password_user(random_password)
    get_username_endp.check_phone_user(random_phone)
    get_username_endp.check_user_status()