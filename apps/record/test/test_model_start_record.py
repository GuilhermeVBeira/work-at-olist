from django.test import TestCase
from django.core.validators import ValidationError
from django.db import IntegrityError
from apps.record.models import StartRecord
from datetime import datetime
import pytz


class StartRecordModelTest(TestCase):

    def test_created(self):
        obj = self.make_obj()
        obj.save()
        self.assertTrue(StartRecord.objects.exists())

    def test_unique_call_id(self):
        obj = self.make_obj()
        obj.save()
        obj2 = self.make_obj()
        with self.assertRaises(IntegrityError):
            obj2.save()

    def test_same_value_source_and_destination(self):
            obj = self.make_obj(source=88888888, destination=88888888)
            with self.assertRaises(ValidationError):
                obj.save()

    def make_obj(self, **kwargs):
        data = {'source': 411234567,
                'destination': 411234569,
                'timestamp': datetime(2018, 11, 20, 20, 8, 7, tzinfo=pytz.UTC),
                'call_id': 3535
                }
        data.update(kwargs)
        obj = StartRecord(**data)
        return obj
