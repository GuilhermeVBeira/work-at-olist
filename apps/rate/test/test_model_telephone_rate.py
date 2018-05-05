from django.test import TestCase
from django.core.validators import ValidationError
# from django.db import IntegrityError
from apps.rate.models import TelphoneRate
from datetime import time


class TelphoneRateModelTest(TestCase):

    def test_created(self):
        """
        Validates if an obj with valid fields saves correctly
        """
        obj = self.make_obj()
        obj.save()
        self.assertTrue(TelphoneRate.objects.exists())

    def test_invalid_start_time(self):
        """
        Invalidate case start time between other rates
        """
        obj = self.make_obj()
        obj.save()
        invalid_time = time(hour=18, minute=0, second=0)
        obj2 = self.make_obj(start=invalid_time)
        with self.assertRaises(ValidationError):
            obj2.save()

    def test_invalid_end_time(self):
        """
        Invalidate case end time between other rates
        """
        obj = self.make_obj()
        obj.save()
        invalid_time = time(hour=19, minute=0, second=0)
        obj2 = self.make_obj(end=invalid_time)
        with self.assertRaises(ValidationError):
            obj2.save()

    def make_obj(self, **kwargs):
        data = {
            'standing_charge': 0.50,
            'charge_minute': 0.10,
            'start': time(hour=18, minute=0, second=0),
            'end': time(hour=22, minute=0, second=0),
            'type': TelphoneRate.TYPE_CHOICE.standard,
        }

        data.update(kwargs)
        obj = TelphoneRate(**data)
        return obj
