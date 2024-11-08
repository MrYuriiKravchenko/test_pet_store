from datetime import datetime
import pytest
import random
import string
from pet.create_pet import CreatePet
from pet.delete_pet import DeletePet
from pet.get_findByStatus import GetPetByStatus
from pet.get_pet import GetPet
from pet.post_pet_petid import PostPetPetid
from pet.put_pet import PutPet
from pet.upload_Image import UploadImage
from store.delete_order_id import Delete
from store.get_store_inventory import GetInventory
from store.get_store_order_id import GetStoreOrderId
from store.post_order import PostOrder


@pytest.fixture()
def pet_creator_endp():
    return CreatePet()

@pytest.fixture()
def upload_image_endp():
    return UploadImage()

@pytest.fixture()
def put_pet_endp():
    return PutPet()

@pytest.fixture()
def pet_get_endp():
    return GetPet()

@pytest.fixture()
def post_pet_petid_endp():
    return PostPetPetid()

@pytest.fixture()
def status_get_status_endp():
    return GetPetByStatus()

@pytest.fixture()
def delete_pet_endp():
    return DeletePet()

@pytest.fixture()
def post_order_endp():
    return PostOrder()

@pytest.fixture()
def get_store_order_id_endp():
    return GetStoreOrderId()

@pytest.fixture()
def get_inventory_endp():
    return GetInventory()

@pytest.fixture()
def delete_oreder_is_endp():
    return Delete()

@pytest.fixture()
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

@pytest.fixture()
def random_id():
    return random.randint(1, 1000)

@pytest.fixture()
def random_pet_status():
    return random.choice(['available', 'pending', 'sold'])

@pytest.fixture()
def current_ship_date():
    ship_date = datetime.utcnow().isoformat() + 'Z'
    return ship_date

@pytest.fixture()
def random_id_order():
    return random.randint(1, 10)

@pytest.fixture()
def create_pet_for_test(pet_creator_endp, random_string, random_id, random_pet_status):
    pet_creator_endp.create_pet(random_id, random_string, random_pet_status)
    return pet_creator_endp

@pytest.fixture()
def create_order_for_test(post_order_endp, random_id, random_id_order, current_ship_date):
    post_order_endp.post_order(random_id, random_id_order, current_ship_date)
    return post_order_endp
