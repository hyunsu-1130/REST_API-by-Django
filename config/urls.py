"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Products API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),      # 베이스 코드 느낌 - api/products/...
    path('apiset/', include('apiset.urls')),       # DRF 느낌 - apiset/products/...
    path('apiviewset/', include('apiviewset.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/', include('tokenapi.urls')),         # 토큰 인증 기능
    path('frontbackdev/', include('frontbackdev.urls')),    # front / back 분리하여 작동
    path('backenlion/', include('backenlion.urls')),    # front / back 분리하여 작동
    path('filter/', include('filterSearch.urls')),    # 검색
]
