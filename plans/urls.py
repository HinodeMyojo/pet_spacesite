from django.urls import path
from django.views.generic import TemplateView
from . import views 

#нужно добавить еще страницу с детальным представлением интернета

app_name = 'plans'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='plans/plans.html'), name='all_plans')
    path('', views.index, name='all_plans')
]
