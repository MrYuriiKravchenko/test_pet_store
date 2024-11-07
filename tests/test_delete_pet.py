def test_delete_pet_store(create_pet_for_test, delete_pet_endp):
    pet_id = create_pet_for_test.pet_id
    delete_pet_endp.delete_pet(pet_id)
    delete_pet_endp.check_response_status_is_ok()
