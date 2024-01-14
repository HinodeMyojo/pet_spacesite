from django.urls import path
from .views import UserProfileDetailView

app_name = 'personal'

urlpatterns = [
    path('<int:pk>', UserProfileDetailView.as_view(), name='personal')
]
