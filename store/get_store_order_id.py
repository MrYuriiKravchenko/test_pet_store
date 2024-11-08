import requests
from store.endpoints_heandler import Endpoint

class GetStoreOrderId(Endpoint):
    order_id = None
    pet_id = None
    quantity_pet = None
    ship_date = None


    def get_order_id(self, order_id):
        response = requests.get(
            f'https://petstore.swagger.io/v2/store/order/{order_id}'
        )
        self.status = response.status_code
        self.order_id = response.json()['id']
        self.pet_Id = response.json()['petId']
        self.quantity_pet = response.json()['quantity']
        self.ship_date = response.json()['shipDate']
        self.status_order = response.json()['status']
        self.complete_order = response.json()['complete']
        return response

    def check_that_the_id_match(self, expected_id_order):
        assert self.order_id == expected_id_order

    def check_petId_same_as_sent(self, expected_petId):
        assert self.pet_Id == expected_petId

    def check_quantity_correct(self, expected_quantity):
        assert self.quantity_pet == expected_quantity

    def check_ship_date_for_order(self, expected_ship_date):
        assert self.ship_date[:19] == expected_ship_date[:19]

    def check_status_place_order(self):
        assert self.status_order == 'placed'

    def check_complete_order(self):
        assert self.complete_order == True