from django.urls import path
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage/homepage.html'), name='homepage'),
]
