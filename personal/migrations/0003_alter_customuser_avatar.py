# Generated by Django 3.2.16 on 2023-12-24 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='defaults/default-avatar.jpg', null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]
