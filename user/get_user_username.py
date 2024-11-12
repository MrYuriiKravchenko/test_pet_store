import requests
from user.endpoints_heandler import Endpoint
from config.config import BASE_URL

class GetUsername(Endpoint):
    user_id = None
    username = None
    first_name = None
    last_name = None
    email = None
    password = None
    phone = None
    user_status = None

    def get_username(self, username):
        response = requests.get(
            f'{BASE_URL}/user/{username}'
        )
        self.status = response.status_code
        self.user_id = response.json()['id']
        self.username = response.json()['username']
        self.first_name = response.json()['firstName']
        self.last_name = response.json()['lastName']
        self.email = response.json()['email']
        self.password = response.json()['password']
        self.phone = response.json()['phone']
        self.user_status = response.json()['userStatus']
        return response

    def check_id_user(self, expected_id):
        assert self.user_id == expected_id

    def check_username(self, expected_username):
        assert self.username == expected_username

    def check_last_name_user(self, expected_last_name):
        assert self.last_name == expected_last_name

    def check_firsrt_name_user(self, expected_first_name):
        assert self.first_name == expected_first_name

    def check_email_user(self, expected_email):
        assert self.email == expected_email

    def check_password_user(self, expected_password):
        assert self.password == expected_password

    def check_phone_user(self, expected_phone):
        assert self.phone == expected_phone

    def check_user_status(self):
        assert self.user_status == 0
