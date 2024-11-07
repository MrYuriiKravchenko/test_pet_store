def test_get_status_pet_store(create_pet_for_test, status_get_status_endp):
    pet_status = create_pet_for_test.pet_status
    status_get_status_endp.get_pet_by_status(pet_status)
    status_get_status_endp.check_response_status_is_ok()
    status_get_status_endp.check_status_in_list(pet_status)
