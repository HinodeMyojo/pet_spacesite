from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('add/', views.NewsCreateView.as_view(), name='news-add'),
    path('<int:pk>/edit/', views.NewsEditView.as_view(), name='news-edit'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news-delete')
]


