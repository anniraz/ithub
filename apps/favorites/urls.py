from django.urls import path

from apps.favorites.views import *


urlpatterns = [
    path('favorites/',FavoriteApiViewSet.as_view()),
    path('myfavorites/',MyFavoritesApiView.as_view()),
    path('myfavorites/<int:pk>/',MyFavoritesRUDApiView.as_view()),
]
