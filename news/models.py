from django.db import models
from datetime import datetime

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    """Represents a category."""

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.'),
        unique=True
    )

    class Meta:
        """Returns a string representation of the model."""

        verbose_name = 'категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название новости')
    text = models.CharField(max_length=5000, verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField('Картинка', upload_to='post_image', blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
        related_name='category'
    )

    class Meta:
        ordering=('created_at',)
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering=('created_at',)
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'


class Like(models.Model):
    news = models.ForeignKey(
        News,
        verbose_name='Новость',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Лайк',
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        verbose_name_plural = 'Лайк'
        verbose_name = 'Лайки'
        constraints = [
            models.UniqueConstraint(fields=['news',
            'author'], name='unique_like')
        ]

    def __str__(self):
        return f'{self.author} любит {self.news}'
