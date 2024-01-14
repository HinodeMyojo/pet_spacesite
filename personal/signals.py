from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import models, get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_human_group(sender, instance, created, **kwargs):
    if created:
        # Получаем или создаем группу "human"
        group, _ = models.Group.objects.get_or_create(name='Человек')
        # Добавить пользователя в группу
        instance.groups.add(group)
