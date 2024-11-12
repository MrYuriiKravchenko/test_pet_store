def test_delete_user_username(delete_user_endp, create_user_for_test):
    username = create_user_for_test.username
    delete_user_endp.delete_user(username)
    delete_user_endp.check_response_status_is_ok()