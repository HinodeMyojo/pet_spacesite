from django.urls import path
from django.views.generic import TemplateView

app_name = 'personal'

urlpatterns = [
    path('', TemplateView.as_view(), name='personal-detail')
]
