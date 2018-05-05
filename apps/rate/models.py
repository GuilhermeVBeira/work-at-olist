from django.db import models
from model_utils import Choices


class TelphoneRate(models.Model):
    TYPE_CHOICE = Choices('standard', 'reduced')

    standing_charge = models.DecimalField(max_digits=5, decimal_places=2)
    charge_minute = models.DecimalField(max_digits=5, decimal_places=2)
    start = models.TimeField()
    end = models.TimeField()
    type = models.CharField(max_length=8, choices=TYPE_CHOICE)
