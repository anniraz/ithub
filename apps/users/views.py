from django.contrib.auth import authenticate,login
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        new_user = authenticate(username=request.POST.get('username'),
            password=request.POST.get('password'),
            )
        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginApiView(generics.CreateAPIView):
    serializer_class=LoginSerializer
    queryset=User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_201_CREATED)
        # return super().post(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
        

    #     return super().create(request, *args, **kwargs)
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

    def perform_create(self, serializer):
        return serializer.save(auth=self.request.user)

# class ProfileApiView(generics.ListAPIView):
#     queryset=Profile
#     serializer_class=ProfileSerializers

    # def perform_create(self, serializer):
    #     return serializer.save(profile=self.request.user)


