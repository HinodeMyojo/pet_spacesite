from django.urls import path
from .views import ProfileDetailView

app_name = 'personal'

urlpatterns = [
    path('<int:pk>', ProfileDetailView.as_view(), name='personal-detail')
]
