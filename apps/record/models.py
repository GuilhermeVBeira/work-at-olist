from django.db import models
from django.core.validators import ValidationError, MinLengthValidator
import uuid


class BaseRecord(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField()
    call_id = models.CharField(max_length=200, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{} {}".format(self.call_id, self.timestamp)


class StartRecord(BaseRecord):
    type = models.CharField(max_length=5, default='start')
    source = models.CharField(max_length=9,
                              validators=[MinLengthValidator(8)])
    destination = models.CharField(max_length=9,
                                   validators=[MinLengthValidator(8)])


class EndRecord(BaseRecord):
    type = models.CharField(max_length=3, default='end')

    def save(self, *args, **kwargs):
        if not StartRecord.objects.filter(call_id=self.call_id).exists():
            msg = "there is no record started with this call_id"
            raise ValidationError(msg)

        st = StartRecord.objects.get(call_id=self.call_id)
        if st.timestamp > self.timestamp:
            msg = "timestamp can not be less than start of recording"
            raise ValidationError(msg)
        super().save(*args, **kwargs)
