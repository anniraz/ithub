from rest_framework.response import Response
from rest_framework import generics,filters,permissions

from django_filters import rest_framework as filter
from .service import Paginations, ProductFilter
from .permissions import *


from .models import *
from .serializers import *


class UserAPIView(generics.ListAPIView):
    serializer_class = UserSerializerList
    queryset = User.objects.all()
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filterset_class=ProductFilter
    search_fields = [ 'username']
    pagination_class=Paginations
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializerList
    queryset = User.objects.all()
    permission_classes=[IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(id=pk)
        user_serial = UserSerializerList(user).data
        reviews = Reviews.objects.filter(auth_id = pk)
        lst = []
        for i in reviews:
            lst.append(i.rating)

        rating_sum = sum(lst)
        if len(lst)<=0:
            rating_sum = 'нет отзывов'
        else:
            rating_sum = round(rating_sum / len(lst), 1)

        user_serial['Reviews'] = rating_sum

        return Response(user_serial)



class DeveloperApiView(generics.ListCreateAPIView):
    queryset=Developer.objects.all()
    serializer_class=DeveloperSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class DeveloperRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Developer.objects.all()
    serializer_class=DeveloperSerializer
    permission_classes=[IsOwnerOrReadOnly]
    

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

class CustomerApiView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class CustomerRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[IsOwnerOrReadOnly]



class ReviewCreateView(generics.ListCreateAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewCreateSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(auth=self.request.user)

# class ProfileApiView(generics.ListAPIView):
#     queryset=Profile
#     serializer_class=ProfileSerializers

    # def perform_create(self, serializer):
    #     return serializer.save(profile=self.request.user)


