import requests
from pet.endpoints_heandler import Endpoint
from config.config import BASE_URL

class PostPetPetid(Endpoint):
    pet_id = None
    name = None
    pet_status = None

    def post_pet_petid_store(self, pet_id, name, pet_status):
        url = f'{BASE_URL}/pet/{pet_id}'
        data = {
            'name': name,
            'status': pet_status
        }
        response = requests.post(url, data=data)
        self.status = response.status_code
        return response
    