import requests
from pet.endpoints_heandler import Endpoint

class UploadImage(Endpoint):
    id_pet = None
    additional_metadata = None

    def upload_image(self, pet_id, image_path, additional_metadata=None):
        data = {'additional_metadata': additional_metadata} if additional_metadata else {}

        with open(image_path, 'rb') as image_file:
            response = requests.post(
                f'https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage',
                files={'file': image_file},
                data=data
            )
        self.status = response.status_code
        self.id_pet = pet_id
        return response


