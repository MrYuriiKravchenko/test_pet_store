import requests
from user.endpoints_heandler import Endpoint

class PostCreateWishArray(Endpoint):
    id_user = None
    username = None
    first_name = None
    last_name = None
    email = None
    password = None
    phone = None
    user_status = None


    def post_createwishlist(self, random_id, random_string, random_password, random_email, random_phone):
        response = requests.post(
            'https://petstore.swagger.io/v2/user/createWithArray',
            headers={'Content-Type': 'application/json'},
            json=[
                {
                    "id": random_id,
                    "username": random_string,
                    "firstName": random_string,
                    "lastName": random_string,
                    "email": random_email,
                    "password": random_password,
                    "phone": random_phone,
                    "userStatus": 0
                }
            ]
        )
        self.status = response.status_code
        return  response
