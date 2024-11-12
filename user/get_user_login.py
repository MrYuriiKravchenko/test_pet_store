import requests
from user.endpoints_heandler import Endpoint
from config.config import BASE_URL

class GetLogin(Endpoint):
    username = None
    password = None

    def get_login(self, username, password):
        response = requests.get(
            f'{BASE_URL}/user/login',
            params={'username': username, 'password': password}
        )
        self.status = response.status_code
        self.message = response.json().get('message')
        return response

    def check_message(self, expected_message):
        assert self.message.startswith(expected_message)
