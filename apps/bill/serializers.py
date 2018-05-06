from rest_framework import serializers
from apps.bill.models import Bill


class BillSerializer(serializers.ModelSerializer):

    started = serializers.SerializerMethodField()
    ended = serializers.SerializerMethodField()
    source = serializers.SerializerMethodField()
    destination = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = ["id", "call_price",
                  "started", "ended",
                  "source", "destination"]

    def get_started(self, obj):
        return obj.start.timestamp

    def get_ended(self, obj):
        return obj.end.timestamp

    def get_source(self, obj):
        return obj.start.source

    def get_destination(self, obj):
        return obj.start.destination
