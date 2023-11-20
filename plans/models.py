from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """
    Абстрактная модель.
    Добавляет к модели дату создания и последнего изменения.
    """
    created_at = models.DateTimeField(auto_now_add=True)

    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True



class PlansOption(BaseModel):
    """База опций связи (Инт, Инт+ТВ и тд.)"""
    option = models.CharField(max_length=128, verbose_name='Опции связи')

class PlansEquipment(BaseModel):
    """База устанавливаемого оборудования

    equipment: тип устанавливаемого оборудования
    cost: стоимости установки оборудования

    """
    equipment = models.CharField(max_length=128, verbose_name='Тип оборудования')
    cost = models.IntegerField(verbose_name='Стоимость установки')

class PlansMonthlySub(BaseModel):
    """Стоимость месячной подписки"""
    price = models.IntegerField(verbose_name='Стоимость месячной подписки')

class PlansPeriod(BaseModel):
    """Период подписки"""
    period = models.IntegerField(verbose_name='Период подписки')

class PlansTitleSpeed(BaseModel):
    """Описание тарифов

    title: название тарифа
    speed: скорость тарифа мб/c
    price, option, equipment, period: связанные таблицы
    """
    title = models.CharField(max_length=128, verbose_name='Название тарифа')
    speed = models.CharField(max_length=128, verbose_name='Скорость тарифа')
    price = models.ForeignKey(
        PlansMonthlySub,
        on_delete=models.SET_NULL,
        null=True)
    option = models.ForeignKey(
        PlansOption,
        on_delete=models.SET_NULL,
        null=True)
    equipment = models.ForeignKey(
        PlansEquipment,
        on_delete=models.SET_NULL,
        null=True)
    period = models.ForeignKey(
        PlansPeriod,
        on_delete=models.SET_NULL,
        null=True)




