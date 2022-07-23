from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.favorites.views import MyFavoritesApiView
from apps.orders.views import MyOrdersListApiView,MyOrdersRUDApiView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.users.urls')),
    path('',include('apps.favorites.urls')),
    path('', include('apps.chat.urls')),
    path('', include('apps.orders.urls')),
    path('myfavorites/',MyFavoritesApiView.as_view()),
    path('myorders/',MyOrdersListApiView.as_view()),
    path('myorders/<int:pk>/',MyOrdersRUDApiView.as_view()),
   #  path('myorders1/',MyOrdersApiView1.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # swagger
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)