from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from titanic_app.views import PassengerViewSet

router = DefaultRouter()
router.register(r'passengers', PassengerViewSet, basename='passenger')

schema_view = get_schema_view(
    openapi.Info(
        title="Titanic API",
        default_version="v1",
        description="API for Titanic dataset",
    ),
    public=True,
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
