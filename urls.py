"""ortnamnsregistret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('api/', include('sagenkarta_rest_api.urls')),
    path('api/es/', include('sagendatabas_es_api.urls')),
    path('opendata/', include('sagendatabas_es_api.opendata.v1.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

    # Test with namespace:
    # path('api/', include('sagenkarta_rest_api.urls', namespace='api-base')),
    # path('api/es/', include('sagendatabas_es_api.urls', namespace='api-es')),
    # path('opendata/', include('sagendatabas_es_api.opendata.v1.urls', namespace='folke-opendata-v1')),
    # Not used anymore:
    # path('api/es-advanced/', include('sagendatabasi_es_api_advanced.urls')),
    # path('api/es-test/', include('sagendatabas_es_api-test.urls')),
    # path('Sagenkarta-Admin/', include('Sagenkarta-Admin.urls')),
    # path('admin/', admin.site.urls),
]