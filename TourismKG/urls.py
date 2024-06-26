from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
=======
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Test API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls')),
]
<<<<<<< HEAD

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3
