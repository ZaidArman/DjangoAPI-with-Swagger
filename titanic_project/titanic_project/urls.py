from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Titanic API",
        default_version="v1",
        description="API for Titanic dataset",
    ),
    public=True,
)

urlpatterns = [
    path('api/', include('titanic_app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]