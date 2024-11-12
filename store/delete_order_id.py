import requests
from store.endpoints_heandler import Endpoint
from config.config import BASE_URL

class Delete(Endpoint):
    order_is = None

    def delete_order(self, order_id):
        response = requests.delete(
            f'{BASE_URL}/store/order/{order_id}'
        )
        self.status = response.status_code
        return response


