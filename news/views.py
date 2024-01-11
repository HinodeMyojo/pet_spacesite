from typing import Any
from django.conf import settings
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, FormView, CreateView, detail
from .models import News, Comment, Category
from django.db.models import Count
from django.urls import reverse, reverse_lazy
from . forms import CommentForm


class NewsCreateView(CreateView):
    model = News
    template_name = "news/create.html"
    fields = ['title', 'text', 'image', 'category']
    success_url = reverse_lazy('news:news-list')

    def form_valid(self, form):
        """
        Указывает автора для поста.
        """
        form.instance.author = self.request.user  # Должно работать корректно
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class NewsEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = News
    template_name = "news/create.html"
    fields = '__all__'
    permission_required = 'news.change_news'

class NewsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = News
    template_name = "news/create.html"
    fields = '__all__'
    permission_required = 'news.delete_news'

class NewsListView(ListView):
    model = News
    template_name = 'news/list.html'

    def get_queryset(self):
        """Вывод определенного кол-во новостей"""
        return self.model.objects.prefetch_related(
            'comment_set'
        ).annotate(
            comment_count=Count('comment')
        )[:settings.NEWS_COUNT_ON_HOME_PAGE]

    # def

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            self.model.objects.prefetch_related('comment_set__author'),
            pk=self.kwargs['news_id']
        )
        return obj
    #Добавляем в QuerySet еще context, связанный с формой комментирования
    #для зарегестрированных пользователей
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['form'] = CommentForm()
        return context

class NewsComment(
    LoginRequiredMixin,
    detail.SingleObjectMixin,
    FormView
):
    model = News
    form_class = CommentForm
    template_name = 'news/detail.html'
    pk_url_kwarg = 'news_id'

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.news = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        post = self.get_object()
        return reverse('news:news-detail', kwargs={'news_id': post.pk})

class CommentBase(LoginRequiredMixin):
    """Базовый класс для работы с комментариями."""
    model = Comment
    news = News
    form_class = CommentForm
    template_name = 'news/detail.html'

    def get_success_url(self):
        """Возвращение в случае успеха"""
        post = self.object.news
        return reverse(
            'news:news-detail', kwargs={'news_id': post.pk})

    def get_queryset(self):
        """Пользователь может работать только со своими комментариями."""
        return self.model.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        """Добавляет информацию о новости (News) в контекст шаблона.
        Этот метод вызывается перед рендерингом шаблона, чтобы передать дополнительные
        переменные в шаблон."""

        context = super().get_context_data(**kwargs)
        comment = self.get_object()
        context['news'] = News.objects.get(pk=comment.news_id)
        return context

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            Comment,
            pk=self.kwargs['comment_id']
        )
        return obj


class CommentUpdate(CommentBase, UpdateView):
    pass



class CommentDelete(CommentBase, DeleteView):
    pass

class CategoryCreateView(CreateView):
    """Класс создания Категорий"""
    model = Category
    template_name = "news/category_create.html"
    fields = ['title', 'description', 'slug']
    success_url = reverse_lazy('news:news-list')
