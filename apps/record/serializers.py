from rest_framework import serializers
from apps.record.models import StartRecord, EndRecord
from model_utils import Choices


class StartRecordSerializer(serializers.ModelSerializer):
    TYPE_CHOICE = Choices('start', 'end')
    type = serializers.ChoiceField(TYPE_CHOICE)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = StartRecord
        fields = ['id', 'type', 'call_id', 'source',
                  'destination', 'timestamp']

    def validate(self, data):
        if data['source'] == data['destination']:
            msg = "Source and destination can't be equals"
            raise serializers.ValidationError(msg)
        return data


class EndRecordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = EndRecord
        fields = ['id', 'call_id', 'timestamp']

    def validate(self, data):
        if not StartRecord.objects.filter(call_id=data['call_id']).exists():
            msg = "there is no record started with this call_id"
            raise serializers.ValidationError(msg)
        st = StartRecord.objects.get(call_id=data['call_id'])
        if st.timestamp > data['timestamp']:
            msg = "timestamp can not be less than start of recording"
            raise serializers.ValidationError(msg)
        return data
