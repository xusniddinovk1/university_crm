from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schem_view = get_schema_view(
    openapi.Info(
        title="API CRM",
        default_version="v1",
        description="University CRM API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="komronbek@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('crm_app.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schem_view.without_ui(cache_timeout=0), name='schem-json'),
    path('', schem_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schem_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
