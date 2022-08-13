from django.urls import path
# from rest_framework import routers
from .views import *

# router=routers.DefaultRouter()
# router.register('user',UserAPIView)

urlpatterns = [
    path('users/',UserAPIView.as_view()),
    # path('user/',UserInfoAPIView.as_view()),
    path('users/developer/',DeveloperApiView.as_view()),
    path('users/developer/<int:pk>/',DeveloperApiView.as_view()),
    path('users/developer/change/<int:pk>/',DeveloperRUDApiView.as_view()),
    path('users/customer/',CustomerApiView.as_view()),
    path('users/customer/<int:pk>/',CustomerApiView.as_view()),
    path('users/customer/change/<int:pk>/',CustomerRUDApiView.as_view()),
    path('users/detail/<int:pk>/',UserDetail.as_view()),


    # path('user/login/',UserLoginApiView.as_view()),
    # path('user/logout/',UserLogoutApiView.as_view()),
    path('review/',ReviewCreateView.as_view()),
    # path('profile/',ProfileApiView.as_view()),


]
