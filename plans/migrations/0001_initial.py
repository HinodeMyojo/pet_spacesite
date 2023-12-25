# Generated by Django 3.2.16 on 2023-12-24 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlansEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('equipment', models.CharField(max_length=128, verbose_name='Тип оборудования')),
                ('cost', models.IntegerField(verbose_name='Стоимость установки')),
            ],
            options={
                'verbose_name': 'Устанавливаемое оборудование',
                'verbose_name_plural': 'Устанавливаемое оборудование',
            },
        ),
        migrations.CreateModel(
            name='PlansOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('option', models.CharField(max_length=128, verbose_name='Опции связи')),
            ],
            options={
                'verbose_name': 'Опции связи',
                'verbose_name_plural': 'Опции связи',
            },
        ),
        migrations.CreateModel(
            name='PlansPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('period', models.IntegerField(verbose_name='Период подписки')),
            ],
            options={
                'verbose_name': 'Период подписки',
                'verbose_name_plural': 'Период подписок',
            },
        ),
        migrations.CreateModel(
            name='PlansSpeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('speed', models.IntegerField(verbose_name='Скорость интернета')),
            ],
            options={
                'verbose_name': 'Скорость интернета',
                'verbose_name_plural': 'Скорость интернета',
            },
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='Название тарифа')),
                ('price', models.IntegerField(null=True, verbose_name='Стоимость месячной подписки')),
                ('is_on_main', models.BooleanField(default=True, verbose_name='Отображение')),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.plansequipment', verbose_name='Оборудование')),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.plansoption', verbose_name='Опция')),
                ('period', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.plansperiod', verbose_name='Период')),
                ('speed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.plansspeed', verbose_name='Скорость интернета')),
            ],
            options={
                'verbose_name': 'Описание тарифа',
                'verbose_name_plural': 'Описание тарифов',
                'ordering': ('price',),
            },
        ),
    ]
