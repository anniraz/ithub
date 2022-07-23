from rest_framework.response import Response
from django_filters import rest_framework as filter
from .service import Paginations, ProductFilter
from .permissions import *
# Create your views here.
from rest_framework import viewsets,generics,filters

from .models import *
from .serializers import *


class UserAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filterset_class=ProductFilter
    search_fields = [ 'username']
    pagination_class=Paginations


# class UserProfile(generics.ListAPIView):
#     serializer_class = UserSerializer
#     # queryset = User.objects.all()

    # def get_queryset(self):
    #     user=self.request.user
    #     return User.objects.get(user=user)

    # def get(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     user = User.objects.get(id=pk)
    #     user_serial = UserSerializer(user).data
    #     reviews = Reviews.objects.filter(auth_id = pk)
    #     lst = []
    #     for i in reviews:
    #         lst.append(i.rating)

    #     rating_sum = sum(lst)
    #     if len(lst)<=0:
    #         rating_sum = 'нет отзывов'
    #     else:
    #         rating_sum = round(rating_sum / len(lst), 1)

    #     user_serial['Reviews'] = rating_sum

    #     return Response(user_serial)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes=[IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(id=pk)
        user_serial = UserSerializer(user).data
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

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

class CustomerApiView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)


class ReviewCreateView(generics.ListCreateAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(auth=self.request.user)

# class ProfileApiView(generics.ListAPIView):
#     queryset=Profile
#     serializer_class=ProfileSerializers

    # def perform_create(self, serializer):
    #     return serializer.save(profile=self.request.user)


