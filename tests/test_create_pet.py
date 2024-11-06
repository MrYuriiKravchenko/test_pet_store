def test_create_pet_store(pet_creator_endp, random_string, random_id, random_pet_status):
    pet_creator_endp.create_pet(random_id, random_string, random_pet_status)
    pet_creator_endp.check_response_status_is_ok()
    pet_creator_endp.check_id_same_as_sent(random_id)
    pet_creator_endp.check_category_is_correct_id_and_name(random_id, random_string)
    pet_creator_endp.check_name_same_as_sent(random_string)
    pet_creator_endp.check_that_photo_urls_are_correct([random_string])
    pet_creator_endp.check_that_tags_id_and_name_are_available(random_id, random_string)
    pet_creator_endp.check_pet_status_available(random_pet_status)

