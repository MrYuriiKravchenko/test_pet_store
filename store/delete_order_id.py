import requests
from store.endpoints_heandler import Endpoint

class Delete(Endpoint):
    order_is = None

    def delete_order(self, order_id):
        response = requests.delete(
            f'https://petstore.swagger.io/v2/store/order/{order_id}'
        )
        self.status = response.status_code
        return response


