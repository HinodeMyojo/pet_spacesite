from django.urls import path
from .views import PlansListView, PlansDetailView


app_name = 'plans'

urlpatterns = [
    path('', PlansListView.as_view(), name='plans-list'),
    path('<int:pk>/', PlansDetailView.as_view(), name='plans-detail')
]
