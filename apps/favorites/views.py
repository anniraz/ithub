from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.favorites.models import Favorite
from apps.favorites.serializers import FavoriteSerializer

# from ...permissions import *

class FavoriteApiViewSet(generics.ListCreateAPIView):
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
        

class MyFavoritesApiView(generics.ListAPIView):
    serializer_class=FavoriteSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user=self.request.user
        return Favorite.objects.filter(user=user)

class MyFavoritesRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=FavoriteSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user=self.request.user
        return Favorite.objects.filter(user=user)