from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class RecordTestAPI(APITestCase):

    def setUp(self):
        self.uri = '/fone-tax/'
        self.client = APIClient()

    def test_list_telefone_tax(self):

        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
