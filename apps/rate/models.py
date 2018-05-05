from django.db import models
from django.core.validators import ValidationError
from django.db.models import Q
from model_utils import Choices


class TelphoneRate(models.Model):
    TYPE_CHOICE = Choices('standard', 'reduced')

    standing_charge = models.DecimalField(max_digits=5, decimal_places=2)
    charge_minute = models.DecimalField(max_digits=5, decimal_places=2)
    start = models.TimeField()
    end = models.TimeField()
    type = models.CharField(max_length=8, choices=TYPE_CHOICE)

    def save(self, *args, **kwargs):

        filter1 = {'start__range': [self.start, self.end]}
        filter2 = {'end__range': [self.start, self.end]}

        if TelphoneRate.objects.filter(Q(**filter1) | Q(**filter2)
                                       ).exclude(id=self.id).exists():
            msg = 'There is already some TAX between this time'
            raise ValidationError(msg)
        super().save(*args, **kwargs)
