import requests
from pet.endpoints_heandler import Endpoint
from config.config import BASE_URL

class DeletePet(Endpoint):
    api_key = 'special-key'

    def delete_pet(self, pet_id):
        response = requests.delete(
            f'{BASE_URL}/pet/{pet_id}',
            headers={'api_key': self.api_key}
        )
        self.status = response.status_code
        return response
