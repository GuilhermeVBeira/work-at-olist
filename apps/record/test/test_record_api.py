from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from apps.record.models import StartRecord
from datetime import datetime
import pytz


class RecordTestAPI(APITestCase):

    def setUp(self):
        self.uri = '/record/'
        self.client = APIClient()
        date = datetime(2018, 4, 28, 18, 0, 0, tzinfo=pytz.UTC)
        data_start = {'type': 'start',
                      'source': 411234567,
                      'destination': 411234569,
                      'timestamp': date,
                      'call_id': 3535}

        self.start = StartRecord.objects.create(**data_start)

    def test_create_start_record(self):

        params = {'type': 'start',
                  'source': 411234567,
                  'destination': 411234569,
                  'timestamp': '2018-04-28T18:00',
                  'call_id': 35365}

        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def test_create_start_record_with_unique_call_id(self):

        params = {'type': 'start',
                  'source': 411234567,
                  'destination': 411234569,
                  'timestamp': '2018-04-28T18:00',
                  'call_id': 3535}

        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))

    def test_create_start_record_same_source_and_destination(self):

        params = {'type': 'start',
                  'source': 88888888,
                  'destination': 88888888,
                  'timestamp': '2018-04-28T18:00',
                  'call_id': 3535}

        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))

    def test_create_end_record(self):

        params = {'type': 'end',
                  'timestamp': '2018-04-28T18:00',
                  'call_id': self.start.call_id}

        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

    def test_create_end_record_with_invalid_timestamp(self):

        params = {'type': 'end',
                  'timestamp': '2018-04-28T15:30',
                  'call_id': self.start.call_id}

        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))

    def test_create_end_record_with_invalid_call_id(self):

        params = {'type': 'end',
                  'timestamp': '2018-04-28T18:00',
                  'call_id': 3455}

        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0} instead.'
                         .format(response.status_code))
