from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserSubscription

UserAdmin.fieldsets += (
    # Добавляем кортеж, где первый элемент — это название раздела в админке,
    # а второй элемент — словарь, где под ключом fields можно указать нужные поля.
    ('Тариф', {'fields': ('plan',)}),
    ('Экстра', {'fields': ('sex', 'avatar', 'date_birth')}),
)

admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserSubscription)