from django.test import TestCase
from django.core.validators import ValidationError
from django.db import IntegrityError
from apps.record.models import StartRecord, EndRecord
from datetime import datetime
import pytz


class EndRecordModelTest(TestCase):

    def setUp(self):
        data_start = {
            'source': 411234567,
            'destination': 411234569,
            'timestamp': datetime(2018, 11, 20, 20, 00, tzinfo=pytz.UTC),
            'call_id': 3535
        }
        self.start = StartRecord.objects.create(**data_start)

    def test_created(self):
        """
        Ensure we can create end record
        """
        obj = self.make_obj()
        obj.save()
        self.assertTrue(EndRecord.objects.exists())

    def test_unique_call_id(self):
        """
        Ensure unique field in DB
        """
        obj = self.make_obj()
        obj.save()
        obj2 = self.make_obj()
        with self.assertRaises(IntegrityError):
            obj2.save()

    def test_invalid_call_id(self):
        """
        Ensure can't create end object without start object save before
        """
        obj = self.make_obj(call_id=123)
        with self.assertRaises(ValidationError):
            obj.save()

    def test_lower_timestamp_than_start(self):
        """
        Ensure can't create end object with time lower than start time
        """
        invalid_date = datetime(2018, 11, 20, 19, 30, tzinfo=pytz.UTC)
        obj = self.make_obj(timestamp=invalid_date)
        with self.assertRaises(ValidationError):
            obj.save()

    def make_obj(self, **kwargs):
        data = {'timestamp': datetime(2018, 11, 20, 20, 30, tzinfo=pytz.UTC)}
        data.update({'call_id': self.start.call_id})
        data.update(kwargs)
        obj = EndRecord(**data)
        return obj
