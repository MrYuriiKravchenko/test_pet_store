import requests
from pet.endpoints_heandler import Endpoint
from config.config import BASE_URL

class GetPetByStatus(Endpoint):
    pet_status = None
    pets = []

    def get_pet_by_status(self, pet_status):
        url = f'{BASE_URL}/pet/findByStatus'
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

