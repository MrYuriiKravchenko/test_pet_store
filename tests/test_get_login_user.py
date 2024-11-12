def test_get_login_user(get_login_user_endp, create_user_for_test):
    username = create_user_for_test.username
    password = create_user_for_test.password
    get_login_user_endp.get_login(username, password)
    get_login_user_endp.check_response_status_is_ok()
    print(get_login_user_endp.message)
    get_login_user_endp.check_message('logged in user session:')