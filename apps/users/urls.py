from django.urls import path
# from rest_framework import routers
from .views import *

# router=routers.DefaultRouter()
# router.register('user',UserAPIView)

urlpatterns = [
    path('users/',UserAPIView.as_view()),
    # path('users/<int:pk>/',UserAPIView.as_view()),
    path('developer/',DeveloperApiView.as_view()),
    path('developer/<int:pk>/',DeveloperApiView.as_view()),
    path('developer/change/<int:pk>/',DeveloperRUDApiView.as_view()),
    path('customer/',CustomerApiView.as_view()),
    path('customer/<int:pk>/',CustomerApiView.as_view()),
    path('customer/change/<int:pk>/',CustomerRUDApiView.as_view()),
    path('users/detail/<int:pk>/',UserDetail.as_view()),
    path('review/',ReviewCreateView.as_view()),
    # path('profile/',ProfileApiView.as_view()),


]
