from rest_framework import serializers
from apps.bill.models import Bill


class BillSerializer(serializers.ModelSerializer):
    bill = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
            view_name='bill-detail',
            read_only=True,
            lookup_field='pk'
        )

    class Meta:
        model = Bill
        fields = ['detail', 'bill']

    def get_bill(self, obj):
        data = [obj.start.call_id, obj.start, obj.end]
        return 'call_id: {}, started at {} and ended at {}.'.format(*data)


class BillDetailSerializer(serializers.ModelSerializer):

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