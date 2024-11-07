def test_post_pet_petid(create_pet_for_test,post_pet_petid_endp):
    pet_id = create_pet_for_test.pet_id
    name = create_pet_for_test.name
    pet_status = create_pet_for_test.pet_status
    post_pet_petid_endp.post_pet_petid_store(pet_id, name, pet_status)
    post_pet_petid_endp.check_response_status_is_ok()

