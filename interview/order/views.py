from rest_framework import generics
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs) -> Response:
        qs = self.get_queryset()
        if request.query_params.get("date"):
            qs = qs.filter(
                start_date__lte=request.query_params["date"],
                embargo_date__gt=request.query_params["date"],
            )

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
