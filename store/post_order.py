import requests
from store.endpoints_heandler import Endpoint

class PostOrder(Endpoint):
    order_id = None
    pet_Id = None
    quantity_pet = None
    ship_date = None
    status_order = None
    complete_order = None

    def post_order(self, random_id, random_id_order, current_ship_date):
        response = requests.post(
            'https://petstore.swagger.io/v2/store/order',
            headers={'Content-Type': 'application/json'},
            json={
                  "id": random_id_order,
                  "petId": random_id,
                  "quantity": random_id,
                  "shipDate": current_ship_date,
                  "status": "placed",
                  "complete": True
                }
        )
        self.status = response.status_code
        self.order_id = response.json()['id']
        self.pet_Id = response.json()['petId']
        self.quantity_pet = response.json()['quantity']
        self.ship_date = response.json()['shipDate']
        self.status_order = response.json()['status']
        self.complete_order = response.json()['complete']
        return response

    def check_check_that_the_id_match(self, expected_id_order):
        assert self.order_id == expected_id_order

    def check_petId_same_as_sent(self, expected_petId):
        assert self.pet_Id == expected_petId

    def check_quantity_correct(self, expected_quantity):
        assert self.quantity_pet == expected_quantity

    def check_ship_date_for_order(self, expected_ship_date):
        assert self.ship_date == expected_ship_date

    def check_status_place_order(self):
        assert self.status_order == 'placed'

    def check_complete_order(self):
        assert self.complete_order == True

