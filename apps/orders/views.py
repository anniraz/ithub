from rest_framework import viewsets,generics
from rest_framework.response import Response

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer,Order1Serializer

class OrdersApiViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    # permission_classes=(IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
        

class MyOrdersListApiView(generics.ListAPIView):
    serializer_class=OrderSerializer

    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)

class MyOrdersRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer

    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)


    # def get(self, request, *args, **kwargs):
    #     # pk = kwargs.get('pk', None)
    #     user=self.request.user
    #     order=Order.objects.filter(user=user)
    #     order_serial=Order1Serializer(order).data
    #     order_lst=[]
    #     for i in order:
    #         order_lst.append(i)
    #     order_serial['My order count'] = len(order_lst)

    #     return Response(order_serial)
        
       
class MyOrdersApiView1(generics.ListAPIView):
# class MyOrdersApiView(generics.ListAPIView):
    serializer_class=OrderSerializer



    def get(self, request, *args, **kwargs):
        # pk = kwargs.get('pk', None)
        user=self.request.user
        order=Order.objects.filter(user=user)
        order_serial=Order1Serializer(order).data
        order_lst=[]
        for i in order:
            order_lst.append(i)
        order_serial['My order count'] = len(order_lst)

        return Response(order_serial)



#     serializer_class=OrderSerializer

#     def get_queryset(self):
#         user=self.request.user
#         return Order.objects.filter(user=user)


    # def get(self, request, *args, **kwargs):
    #     # pk = kwargs.get('pk', None)
    #     user=self.request.user
    #     order=Order.objects.filter(user=user)
    #     order_serial=OrderSerializer(order).data
    #     order_lst=[]
    #     for i in order:
    #         order_lst.append(i.to_user)
    #     order_serial['My order count'] = len(order_lst)

    #     return Response(order_serial)



