"""hospital_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    # path('account/', include('account.urls')),
    path('patient/', include('patient.urls')),
    path('medicine/', include('medicine.urls')),
    path('settingapp/', include('settingapp.urls')),
    path('appointment/', include('appointment.urls')),

    # path('auth/', include('account.admin_urls')),
    path('auth/', include('hospital.admin_urls')),
    path('auth/', include('medicine.admin_urls')),
    path('auth/', include('patient.admin_urls')),
    path('auth/', include('appointment.admin_urls')),
    path('auth/', include('settingapp.admin_urls')),

    # API
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('hospital.api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)