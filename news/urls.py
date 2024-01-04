from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news-list'),
    path('<int:news_id>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('add/', views.NewsCreateView.as_view(), name='news-add'),
    path('<int:news_id>/edit/', views.NewsEditView.as_view(), name='news-edit'),
    path('<int:news_id>/delete/', views.NewsDeleteView.as_view(), name='news-delete'),
    path('<int:news_id>/comment/add/', views.NewsComment.as_view(), name='comment-add'),
    path('<int:news_id>/comment/<int:comment_id>/edit/', views.CommentUpdate.as_view(), name='comment-edit'),
    path('<int:news_id>/comment/<int:comment_id>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
]
