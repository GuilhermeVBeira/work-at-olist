from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.record.models import EndRecord, StartRecord
from apps.bill.models import Bill


@receiver(post_save, sender=EndRecord)
def create_bill(sender, instance=None, created=False, **kwargs):
    if created:
        start = StartRecord.objects.get(call_id=instance.call_id)
        Bill.objects.create(start=start, end=instance)
