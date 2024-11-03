import requests
from pet.endpoints_heandler import Endpoint

class CreatePet(Endpoint):
    id = None
    category_id = None
    category_name = None
    name = None
    photo_urls = []
    tags = []
    pet_status = None

    def create_pet(self):
        response = requests.post(
            'https://petstore.swagger.io/v2/pet',
            headers={'Content-Type': 'application/json'},
            json={
                  "id": 78,
                  "category": {
                    "id": 2,
                    "name": "Dogs"
                  },
                  "name": "Barsik",
                  "photoUrls": [
                    "string.png"
                  ],
                  "tags": [
                    {
                      "id": 99,
                      "name": "doggie_style"
                    }
                  ],
                  "status": "available"
                }
        )
        self.status = response.status_code
        self.id = response.json()['id']
        self.category_id = response.json()['category']['id']
        self.category_name = response.json()['category']['name']
        self.name = response.json()['name']
        self.photo_urls = response.json()['photoUrls']
        self.tags = response.json()['tags']
        self.pet_status = response.json()['status']
        return response

    def check_id_same_as_sent(self):
        assert self.id == 78

    def check_category_is_correct_id_and_name(self):
        assert self.category_id == 2
        assert self.category_name == 'Dogs'

    def check_name_same_as_sent(self):
        assert self.name == 'Barsik'

    def check_that_photo_urls_are_correct(self):
        assert self.photo_urls == ['string.png']

    def check_that_tags_id_and_name_are_available(self):
        assert len(self.tags) > 0
        assert self.tags[0]['id'] == 99
        assert self.tags[0]['name'] == 'doggie_style'

    def check_pet_status_available(self):
        assert self.pet_status == 'available'

