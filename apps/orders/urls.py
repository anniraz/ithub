from rest_framework.routers import DefaultRouter

from apps.orders.views import OrdersApiViewSet

router = DefaultRouter()
router.register(
    prefix='orders',
    viewset=OrdersApiViewSet
)
urlpatterns = router.urls
