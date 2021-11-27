from django.conf import settings
from django.conf.urls import url
from django.urls import include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Conference Management System API",
        default_version="v1",
        description="Conference Management System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    re_path(r'^api/v1/', include('conferences.urls')),
    re_path(r'^api/v1/', include('participants.urls')),
    re_path(r'^api/v1/', include('talks.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
            ),
        url(r'redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'
            ),
    ]
