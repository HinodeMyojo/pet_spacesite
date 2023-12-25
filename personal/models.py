from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    MAN = 'Муж.'
    WOMAN = 'Жен.'
    SHREK = 'Шрек'
    SEXS = [
        (MAN, 'Мужчина'),
        (WOMAN, 'Женщина'),
        (SHREK, 'Шрек'),
    ]
    sex = models.CharField(
        'Пол',
        max_length=5,
        choices=SEXS,
        default=SHREK,
    )

    avatar = models.ImageField(
        'Аватар',
        blank=True,
        null=True,
        upload_to='avatars/',# Изменено на upload_to с путем к папке 'avatars/'
        default='defaults/default-avatar.jpg',
    )