import pytest
import random
import string
from pet.create_pet import CreatePet
from pet.put_pet import PutPet
from pet.upload_Image import UploadImage

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
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

@pytest.fixture()
def random_id():
    return random.randint(1, 10000)

@pytest.fixture()
def random_pet_status():
    return random.choice(['available', 'pending', 'sold'])

@pytest.fixture()
def create_pet_for_test(pet_creator_endp, random_string, random_id, random_pet_status):
    pet_creator_endp.create_pet(random_id, random_string, random_pet_status)
    return pet_creator_endp

