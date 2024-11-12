import requests
from store.endpoints_heandler import Endpoint
from config.config import BASE_URL

class GetInventory(Endpoint):
    response_json = None

    def get_inventory(self):
        response = requests.get(
            f'{BASE_URL}/store/inventory'
        )
        self.status = response.status_code
        self.response_json = response.json()
        return response

    def check_response_contains_dict(self):
        assert isinstance(self.response_json, dict)
