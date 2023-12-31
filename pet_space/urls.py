"""pet_space URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='home')),
    path('plans/', include('plans.urls', namespace='plans')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', views.RegistrationView.as_view(
    ), name='registration'),
    path('profile/', include('personal.urls', namespace='personal')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('news/', include('news.urls', namespace='news')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)