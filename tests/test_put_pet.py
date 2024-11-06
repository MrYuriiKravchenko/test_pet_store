def test_pet_put_store(create_pet_for_test, put_pet_endp, random_id, random_string, random_pet_status):
    pet_id = create_pet_for_test.pet_id
    put_pet_endp.put_pet(pet_id, random_id, random_string, random_pet_status)
    put_pet_endp.check_response_status_is_ok()
    put_pet_endp.check_check_that_the_id_match(pet_id)
    put_pet_endp.check_category_is_correct_id_and_name(random_id, random_string)
    put_pet_endp.check_name_same_as_sent(random_string)
    put_pet_endp.check_that_photo_urls_are_correct([random_string])
    put_pet_endp.check_that_tags_id_and_name_are_available(random_id, random_string)
    put_pet_endp.check_pet_status_available(random_pet_status)
