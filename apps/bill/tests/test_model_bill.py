from django.test import TestCase
from apps.bill.models import Bill
from apps.record.models import StartRecord, EndRecord
from apps.rate.models import TelphoneRate
from datetime import datetime, time
import pytz


class BillModelTest(TestCase):

    def setUp(self):
        # data for start record
        start_date = datetime(2018, 11, 20, 21, 57, 13, tzinfo=pytz.UTC)
        data_start = {'source': 411234567, 'destination': 411234569,
                      'timestamp': start_date, 'call_id': 3535}
        # data for end record
        end_date = datetime(2018, 11, 20, 22, 10, 56, tzinfo=pytz.UTC)
        data_end = {'timestamp': end_date, 'call_id': 3535}
        # data for first telefone tax
        data_tax1 = {'standing_charge': 0.36,
                     'charge_minute': 0.09,
                     'start': time(hour=6, minute=0, second=0),
                     'end': time(hour=22, minute=0, second=0),
                     'type': TelphoneRate.TYPE_CHOICE.standard}
        # data for second telefone tax
        data_tax2 = {'standing_charge': 0.36,
                     'charge_minute': 0.00,
                     'start': time(hour=22, minute=0, second=0),
                     'end': time(hour=6, minute=0, second=0),
                     'type': TelphoneRate.TYPE_CHOICE.standard}
        self.start = StartRecord.objects.create(**data_start)
        self.end = EndRecord.objects.create(**data_end)
        self.tax1 = TelphoneRate.objects.create(**data_tax1)
        self.tax2 = TelphoneRate.objects.create(**data_tax2)

    def test_created(self):
        """
        Validates if an obj with valid fields saves correctly
        """
        obj = self.make_obj()
        obj.save()
        self.assertTrue(Bill.objects.exists())

    def test_calculation(self):
        """
        Ensure the call_price will be calculated correctly
        """
        obj = self.make_obj()
        obj.save()
        self.assertEqual(float(obj.call_price), 0.54)

    def make_obj(self, **kwargs):
        data = {'start': self.start, 'end': self.end}
        data.update(kwargs)
        obj = Bill(**data)
        return obj
