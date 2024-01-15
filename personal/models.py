from django.db import models
from django.contrib.auth.models import AbstractUser
from plans.models import Plans
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    class SexChoices(models.TextChoices):
        MAN = 'Муж.', 'Мужчина'
        WOMAN = 'Жен.', 'Женщина'
        SHREK = 'Шрек', 'Шрек'
    sex = models.CharField(
        'Пол',
        max_length=5,
        choices=SexChoices.choices,
        default=SexChoices.SHREK,
    )

    avatar = models.ImageField(
        'Аватар',
        blank=True,
        null=True,
        upload_to='avatars/',# Изменено на upload_to с путем к папке 'avatars/'
        default='defaults/default-avatar.jpg',
    )
    date_birth = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )
    plan = models.ForeignKey(
        Plans,
        on_delete=models.SET_NULL,
        null=True,
        related_name='users_plan'
        )
    phone_number = PhoneNumberField(
        'Номер телефона',
        null=True,
        blank=True,
        unique=True
        )