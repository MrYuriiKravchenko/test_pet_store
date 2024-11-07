import requests
from pet.endpoints_heandler import Endpoint

class GetPetByStatus(Endpoint):
    pet_status = None
    pets = []

    def get_pet_by_status(self, pet_status):
        url = 'https://petstore.swagger.io/v2/pet/findByStatus'
        params = {
            'status': pet_status
        }
        response = requests.get(url, params=params)
        self.status = response.status_code
        self.pets = response.json()
        return response.json()

    def check_status_in_list(self, expected_status):
        for pet in self.pets:
            assert pet['status'] == expected_status

