from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class RecordTestAPI(APITestCase):

    def setUp(self):
        self.uri = '/bill/'
        self.client = APIClient()

    def test_list_bill(self):
        """
        Ensure we can list bill objects.
        """
        uri = self.uri+"?subscriber=444"
        response = self.client.get(uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_list_bill_without_subscriber(self):
        """
        Ensure we can validate miss subscriber
        """
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))

    def test_list_bill_with_valid_reference(self):
        """
        Ensure we can get list with valid reference
        """
        uri = self.uri+"?subscriber=444&reference=02/2018"
        response = self.client.get(uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_list_bill_with_invalid_reference(self):
        """
        Ensure we can invalidate reference
        """
        uri = self.uri+"?subscriber=444&reference=13/2018"
        response = self.client.get(uri)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))
