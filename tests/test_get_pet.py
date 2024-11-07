def test_get_pet_store(create_pet_for_test, pet_get_endp, random_string, random_pet_status, random_id):
    pet_id = create_pet_for_test.pet_id
    pet_get_endp.get_pet(pet_id)
    pet_get_endp.check_response_status_is_ok()
    pet_get_endp.check_check_that_the_id_match(pet_id)
    pet_get_endp.check_category_is_correct_id_and_name(random_id, random_string)
    pet_get_endp.check_name_same_as_sent(random_string)
    pet_get_endp.check_that_photo_urls_are_correct([random_string])
    pet_get_endp.check_that_tags_id_and_name_are_available(random_id, random_string)
    pet_get_endp.check_pet_status_available(random_pet_status)
