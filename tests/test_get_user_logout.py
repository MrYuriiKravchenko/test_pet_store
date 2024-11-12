def test_get_user_logout(get_user_logout_endp, create_user_for_test):
    get_user_logout_endp.user_logout()
    get_user_logout_endp.check_response_status_is_ok()
