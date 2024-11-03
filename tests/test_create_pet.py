def test_create_pet_store(pet_creator_endp):
    pet_creator_endp.create_pet()
    pet_creator_endp.check_response_status_is_ok()
    pet_creator_endp.check_id_same_as_sent()
    pet_creator_endp.check_category_is_correct_id_and_name()
    pet_creator_endp.check_name_same_as_sent()
    pet_creator_endp.check_that_photo_urls_are_correct()
    pet_creator_endp.check_that_tags_id_and_name_are_available()
    pet_creator_endp.check_pet_status_available()

