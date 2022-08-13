from django.urls import path

from apps.orders.views import *


urlpatterns = [
    path('orders/',OrdersListCreateApiView.as_view()),
    path('orders/<int:pk>/',OrdersRetriveDestroyApiView.as_view()),
    path('myorders/',MyOrdersListApiView.as_view()),
    path('orders/to/me/',OrdersToMeListApiView.as_view()),
    path('myorders/<int:pk>/',MyOrdersRUDApiView.as_view()),
    path('myorders/count/',MyOrdersCountApiView.as_view()),
]
