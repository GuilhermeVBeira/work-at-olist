from rest_framework.serializers import ModelSerializer
from apps.rate.models import TelphoneRate


class TelephoneRateSerializer(ModelSerializer):
    class Meta:
        model = TelphoneRate
        fields = "__all__"
