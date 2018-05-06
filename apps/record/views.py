from rest_framework import status
from apps.record.serializers import StartRecordSerializer, EndRecordSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets


class RecordViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Start or end records
    """
    serializer_class = StartRecordSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        type = request.data.get('type', None)
        serializer = self.get_serializer(data=request.data)
        if type == 'end':
            serializer = self.get_serializer_end_record(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers
                        )

    def get_serializer_end_record(self, *args, **kwargs):
        serializer_class = EndRecordSerializer
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
