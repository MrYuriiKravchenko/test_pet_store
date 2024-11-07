import requests
from pet.endpoints_heandler import Endpoint

class PostPetPetid(Endpoint):
    pet_id = None
    name = None
    pet_status = None

    def post_pet_petid_store(self, pet_id, name, pet_status):
        url = f'https://petstore.swagger.io/v2/pet/{pet_id}'
        data = {
            'name': name,
            'status': pet_status
        }
        response = requests.post(url, data=data)
        self.status = response.status_code
        return response
    