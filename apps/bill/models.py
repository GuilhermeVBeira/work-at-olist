from django.db import models
from django.db.models import Q
from apps.rate.models import TelphoneRate
from decimal import Decimal
from datetime import timedelta


class Bill(models.Model):
    start = models.ForeignKey('record.StartRecord', on_delete=models.CASCADE)
    end = models.ForeignKey('record.EndRecord', on_delete=models.CASCADE)
    call_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    @property
    def call_duration(self):
        amount = self.end.timestamp - self.start.timestamp
        return str(amount)

    def __str__(self):
        data = [self.start.call_id, self.start.timestamp, self.end.timestamp]
        return "call_id: {}, started at {} and ended at {}".format(*data)

    @property
    def minutes(self):
        amount = self.end.timestamp - self.start.timestamp
        return int(amount.seconds/60)

    def save(self, *args, **kwargs):
        self.calculate_price()
        super().save(*args, **kwargs)

    def calculate_price(self):
        # start vars
        amount_price = 0
        end = self.end.timestamp.time()
        start = self.start.timestamp.time()

        # make filters
        # date match with end of tax
        data1 = {'start__lte': end, 'end__gte': end}
        # date match with start of tax
        data2 = {'start__lte': start, 'end__gte': start}

        # tax inside obj date range
        data3 = {'start__gte': start, 'end__lte': end}
        # obj date inside tax range
        data4 = {'start__lte': start, 'end__gte': end}

        # checks all rates at which the call combines
        tax_to_appy = TelphoneRate.objects.filter(
            Q(**data1) | Q(**data2) | Q(**data3) | Q(**data4)
        ).order_by('start').distinct()
        # tax_to_appy = tax_to_appy.order_by('start')
        for tax in tax_to_appy:

            if tax.start <= start and tax.end >= end:
                # obj date inside tax range
                amount_price += Decimal(self.minutes) * tax.charge_minute
            if tax.start > start and tax.end < end:
                # tax inside obj date range
                amount_price += Decimal(self.minutes) * tax.charge_minute

            if tax.start >= start and tax.end >= end:
                # date match with end of tax
                diff = to_timedelta(end) - to_timedelta(tax.start)
                minutes = int(diff.seconds/60)
                amount_price += Decimal(minutes) * tax.charge_minute

            if tax.start <= start and tax.end <= end:
                # date match with start of tax
                diff = to_timedelta(tax.end) - to_timedelta(start)
                minutes = int(diff.seconds/60)
                amount_price += Decimal(minutes) * tax.charge_minute

        # apply standing_charge
        if len(tax_to_appy) > 0:
            amount_price += tax_to_appy[0].standing_charge
        self.call_price = amount_price


def to_timedelta(date1):
    # convert datetime to support operator -
    data = {'hours': date1.hour,
            'minutes': date1.minute,
            'seconds': date1.second}

    return timedelta(**data)
