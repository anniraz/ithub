from rest_framework import viewsets,generics,permissions
from rest_framework.response import Response

from apps.orders.models import Order,MakeOrder
from apps.orders.serializers import OrderSerializer,MakeOrderSerializer

from .permissions import *

class MakeOrdersListCreateApiView(generics.ListCreateAPIView):
    queryset=MakeOrder.objects.all()
    serializer_class=MakeOrderSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class OrdersListCreateApiView(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class OrdersRetriveDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=MakeOrder.objects.all()
    serializer_class=MakeOrderSerializer
    permission_classes=(IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class MyOrdersListApiView(generics.ListAPIView):
    serializer_class=OrderSerializer

    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)

class OrdersToMeListApiView(generics.ListAPIView):
    serializer_class=OrderSerializer

    def get_queryset(self):
        user=self.request.user
        for i in MakeOrder.objects.all():
            if user==i.user:
                print(user)
                return Order.objects.filter(to_user=i)
                

class MyOrdersRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer

    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)



class MyOrdersCountApiView(generics.ListAPIView):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()

    def get(self, request, *args, **kwargs):
        user=self.request.user
        order_count=Order.objects.filter(   user=user).count()
        return Response({'My orders count':order_count})



class MyOrdersRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer

    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)


       

