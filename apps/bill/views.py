from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from apps.bill.serializers import BillSerializer, BillDetailSerializer
from apps.bill.models import Bill
from datetime import datetime


class BillViewSet(viewsets.ViewSet):
    """

    """

    def list(self, request):
        origin = request.GET.get('subscriber', None)
        reference = request.GET.get('reference', None)

        if origin is None:
            msg = 'Please insert a subscriber'
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        queryset = Bill.objects.filter(start__source=origin)
        if reference is not None:
            # check if reference is correct date format
            try:
                d = datetime.strptime(reference, '%m/%Y')
                data = {'end__timestamp__year': d.year,
                        'end__timestamp__month': d.month}

            except ValueError as e:
                msg = 'Please insert a valid date fomat %m/%Y'
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            # filter by last month
            now = datetime.now()
            month = now.month - 1
            data = {'end__timestamp__year': now.year,
                    'end__timestamp__month': month}

        queryset = queryset.filter(**data)
        ctx = {'request': request}
        serializer = BillSerializer(queryset, context=ctx, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Bill.objects.all()
        bill = get_object_or_404(queryset, pk=pk)
        serializer = BillDetailSerializer(bill)
        return Response(serializer.data)
