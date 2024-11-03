import pytest
from pet.create_pet import CreatePet

@pytest.fixture()
def pet_creator_endp():
    return CreatePet()

