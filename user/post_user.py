import requests
from user.endpoints_heandler import Endpoint

class PostUser(Endpoint):

    def post_user(self, random_id, random_string, random_password, radom_email, random_phone):

        response = requests.post(
            'https://petstore.swagger.io/v2/user',
            headers={'Content-Type': 'application/json'},
            json={
                  "id": random_id,
                  "username": random_string,
                  "firstName": random_string,
                  "lastName": random_string,
                  "email": radom_email,
                  "password": random_password,
                  "phone": random_phone,
                  "userStatus": 0
                }
        )
        self.status = response.status_code
        self.username = random_string
        return response
