import requests
from user.endpoints_heandler import Endpoint
from config.config import BASE_URL


class DeleteUsername(Endpoint):
    username = None

    def delete_user(self, username):
        response = requests.delete(
            f'{BASE_URL}/user/{username}',
        )
        self.status = response.status_code
        return response
