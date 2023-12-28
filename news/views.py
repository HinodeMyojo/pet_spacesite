from typing import Any
from django.conf import settings
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, FormView, CreateView, detail
from .models import News, Comment, Category
from django.db.models import Count
from django.urls import reverse
from . forms import CommentForm

class NewsCreateView(CreateView):
    model = News
    template_name = "news/create.html"
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class NewsEditView(UpdateView):
    model = News
    template_name = "news/create.html"
    fields = '__all__'

class NewsDeleteView(DeleteView):
    model = News
    template_name = "news/create.html"
    fields = '__all__'

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

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'

    def get_object(self, queryset=None): 
        obj = get_object_or_404( 
            self.model.objects.prefetch_related('comment_set__author'), 
            pk=self.kwargs['pk'] 
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
        return reverse('news:detail', kwargs={'pk':post.pk}) + '#comments'

class CommentBase(LoginRequiredMixin):
    """Базовый класс для работы с комментариями."""
    model = Comment

    def get_success_url(self):
        comment = self.get_objcet()
        return reverse(
            'news:detail', kwargs={'pk': comment.news.pk}
        ) + '#comments'

    def get_queryset(self):
        """Пользователь может работать только со своими комментариями."""
        return self.model.objects.filter(author=self.request.user)


class CommentUpdate(CommentBase, UpdateView):
    template_name = 'news/edit.html'
    form_class = CommentForm

class CommentDelete(CommentBase, DeleteView):
    template_name = 'news/delete.html'
