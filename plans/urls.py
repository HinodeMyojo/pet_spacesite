from django.urls import path
from . import views 


app_name = 'plans'

urlpatterns = [
    path('', views.index, name='all_plans'),
    path('<int:pk>/', views.detail, name='detail_plan')
]
