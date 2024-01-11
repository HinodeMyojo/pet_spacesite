from django.urls import path
from .views import CustomUserUpdateView

app_name = 'personal'

urlpatterns = [
    path('<int:pk>', CustomUserUpdateView.as_view(), name='personal')
]
