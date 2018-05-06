from apps.rate.serializers import TelephoneRateSerializer
from apps.rate.models import TelphoneRate
from rest_framework import mixins
from rest_framework import viewsets


class TelephoneRateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = TelephoneRateSerializer
    permission_classes = ()
    queryset = TelphoneRate.objects.all()
