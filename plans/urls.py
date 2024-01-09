from django.urls import path
from .views import PlansListView, PlansDetailView
from django.views.generic import TemplateView


app_name = 'plans'

urlpatterns = [
    path('', PlansListView.as_view(), name='plans-list'),
    path('<int:pk>/', PlansDetailView.as_view(), name='plans-detail'),
    path('ilovelika/', TemplateView.as_view(template_name = 'plans/ilovelika.html'), name='lika'),
]
