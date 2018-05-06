from rest_framework import serializers
from apps.bill.models import Bill


class BillSerializer(serializers.ModelSerializer):

    duration = serializers.SerializerMethodField()
    started_date = serializers.SerializerMethodField()
    started_time = serializers.SerializerMethodField()
    destination = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = ["destination",
                  "started_date",
                  "started_time",
                  "duration",
                  "call_price"]

    def get_destination(self, obj):
        return obj.start.destination

    def get_started_date(self, obj):
        return obj.start.timestamp.date()

    def get_started_time(self, obj):
        return obj.end.timestamp.time()

    def get_duration(self, obj):
        return obj.call_duration
