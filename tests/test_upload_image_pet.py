def test_upload_image(create_pet_for_test, upload_image_endp, random_string):
    pet_id = create_pet_for_test.pet_id
    image_path = '/home/yurii/Изображения/kto-i-kakie-stavit-avatarki-x-d3b.png'
    upload_image_endp.upload_image(pet_id, image_path, random_string)
    upload_image_endp.check_response_status_is_ok()


