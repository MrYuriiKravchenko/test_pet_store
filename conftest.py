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
from user.delete_user_username import DeleteUsername
from user.get_user_login import GetLogin
from user.get_user_logout import GetUserLogout
from user.get_user_username import GetUsername
from user.post_createwishlist import PostCreateWishlist
from user.post_createwitharray import PostCreateWishArray
from user.post_user import PostUser
from user.put_user_username import PutUser


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
def post_createwishlist_endp():
    return PostCreateWishlist()

@pytest.fixture()
def post_createwisharrey_endp():
    return PostCreateWishArray()

@pytest.fixture()
def post_user_endp():
    return PostUser()

@pytest.fixture()
def get_username_endp():
    return GetUsername()

@pytest.fixture()
def put_user_endp():
    return PutUser()

@pytest.fixture()
def delete_user_endp():
    return DeleteUsername()

@pytest.fixture()
def get_login_user_endp():
    return GetLogin()

@pytest.fixture()
def get_user_logout_endp():
    return GetUserLogout()

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
def radom_email():
    domain = random.choice(['example.com', 'test.com','mail.com'])
    return f"{''.join(random.choices(string.ascii_lowercase, k=8))}@{domain}"

@pytest.fixture()
def random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

@pytest.fixture()
def random_phone():
    country_code = "+7"
    operator_code = random.randint(900, 999)
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"{country_code}{operator_code}{number}"

@pytest.fixture()
def create_pet_for_test(pet_creator_endp, random_string, random_id, random_pet_status):
    pet_creator_endp.create_pet(random_id, random_string, random_pet_status)
    return pet_creator_endp

@pytest.fixture()
def create_order_for_test(post_order_endp, random_id, random_id_order, current_ship_date):
    post_order_endp.post_order(random_id, random_id_order, current_ship_date)
    return post_order_endp

@pytest.fixture()
def create_user_for_test(post_user_endp, random_id, random_string, random_password, radom_email, random_phone):
    post_user_endp.post_user(random_id, random_string, random_password, radom_email, random_phone)
    return post_user_endp
