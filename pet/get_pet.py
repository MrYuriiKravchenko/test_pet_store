import requests
from pet.endpoints_heandler import Endpoint

class GetPet(Endpoint):
    pet_id = None
    def get_pet(self, pet_id):
        response = requests.get(
            f'https://petstore.swagger.io/v2/pet/{pet_id}',
            headers={'Content-Type': 'application/json'},
        )
        self.status = response.status_code
        self.pet_id = response.json()['id']
        self.category_id = response.json()['category']['id']
        self.category_name = response.json()['category']['name']
        self.name = response.json()['name']
        self.photo_urls = response.json()['photoUrls']
        self.tags = response.json()['tags']
        self.pet_status = response.json()['status']
        return response

    def check_check_that_the_id_match(self, expected_id):
        assert self.pet_id == expected_id

    def check_category_is_correct_id_and_name(self, expected_id, expected_name):
        assert self.category_id == expected_id
        assert self.category_name == expected_name

    def check_name_same_as_sent(self, expected_name):
        assert self.name == expected_name

    def check_that_photo_urls_are_correct(self, expected_photo_urls):
        assert self.photo_urls == expected_photo_urls

    def check_that_tags_id_and_name_are_available(self, expected_tag_id, expected_tag_name):
        assert len(self.tags) > 0
        assert self.tags[0]['id'] == expected_tag_id
        assert self.tags[0]['name'] == expected_tag_name

    def check_pet_status_available(self, expected_status):
        assert self.pet_status == expected_status