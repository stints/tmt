from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=["get"])
    def tags(self, request, pk=None):
        """Get all tags for a specific order"""
        order = self.get_object()
        tags = order.tags.all()
        serializer = OrderTagSerializer(tags, many=True)
        return Response(serializer.data)


class OrderTagListCreateView(viewsets.ModelViewSet):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
