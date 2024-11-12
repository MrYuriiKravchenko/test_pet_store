import requests
from user.endpoints_heandler import Endpoint
from config.config import BASE_URL

class GetUserLogout(Endpoint):

    def user_logout(self):
        response = requests.get(
            f'{BASE_URL}/user/logout'
        )
        self.status = response.status_code
        return response
