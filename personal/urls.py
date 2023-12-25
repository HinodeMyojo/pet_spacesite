from django.urls import path
from django.views.generic import TemplateView

app_name = 'personal'

urlpatterns = [
    path('', TemplateView.as_view(template_name="personal/profile.html"), name='personal-detail')
]
