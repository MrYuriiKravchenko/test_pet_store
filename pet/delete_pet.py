import requests
from pet.endpoints_heandler import Endpoint

class DeletePet(Endpoint):
    api_key = 'special-key'

    def delete_pet(self, pet_id):
        response = requests.delete(
            f'https://petstore.swagger.io/v2/pet/{pet_id}',
            headers={'api_key': self.api_key}
        )
        self.status = response.status_code
        return response
