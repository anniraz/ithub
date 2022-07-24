from django.urls import path
# from rest_framework import routers
from .views import *

# router=routers.DefaultRouter()
# router.register('user',UserAPIView)

urlpatterns = [
    path('user/',UserAPIView.as_view()),
    # path('users/<int:pk>/',UserAPIView.as_view()),
    path('user/developer/',DeveloperApiView.as_view()),
    path('user/developer/<int:pk>/',DeveloperApiView.as_view()),
    path('user/developer/change/<int:pk>/',DeveloperRUDApiView.as_view()),
    path('user/customer/',CustomerApiView.as_view()),
    path('user/customer/<int:pk>/',CustomerApiView.as_view()),
    path('user/customer/change/<int:pk>/',CustomerRUDApiView.as_view()),
    path('users/detail/<int:pk>/',UserDetail.as_view()),
    path('review/',ReviewCreateView.as_view()),
    # path('profile/',ProfileApiView.as_view()),


]
