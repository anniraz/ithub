from django.urls import path
from .views import * 
urlpatterns = [
    path('my_sends/',ChatApiView.as_view()),
    # path('chat/<int:pk>/',ChatDetailApiView.as_view()),
    path('to_me/',ChatToMeApiView.as_view()),
   
]