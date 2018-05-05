from django.db import models


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
