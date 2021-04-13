"""neighbourhood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hood.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/logout", views.logout_then_login, name= "logout"),
    path('tinymce/', include('tinymce.urls')),
    path('api-token-auth/', obtain_auth_token)
]

admin.site.index_title="Neighborhood"
admin.site.site_header="Neighborhood Admin"
admin.site.site_title="Neighborhood"
