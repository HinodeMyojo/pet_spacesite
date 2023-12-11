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
    class Meta:
        verbose_name = 'Опции связи'
        verbose_name_plural = 'Опции связи'
    def __str__(self):
        return self.option

class PlansEquipment(BaseModel):
    """База устанавливаемого оборудования

    equipment: тип устанавливаемого оборудования
    cost: стоимости установки оборудования

    """
    equipment = models.CharField(max_length=128, verbose_name='Тип оборудования')
    cost = models.IntegerField(verbose_name='Стоимость установки')
    class Meta:
        verbose_name = 'Устанавливаемое оборудование'
        verbose_name_plural = 'Устанавливаемое оборудование'
    def __str__(self):
        return self.equipment
    
class PlansPeriod(BaseModel):
    """Период подписки"""
    period = models.IntegerField(verbose_name='Период подписки')
    class Meta:
        verbose_name = 'Период подписки'
        verbose_name_plural = 'Период подписок'
    def __str__(self):
        return str(self.period)
    

class PlansSpeed(BaseModel):
    speed = models.IntegerField(verbose_name='Скорость интернета')
    class Meta:
        verbose_name = 'Скорость интернета'
        verbose_name_plural = 'Скорость интернета'
    def __str__(self):
        return str(self.speed)

class Plans(BaseModel):
    """Описание тарифов

    title: название тарифа
    speed: скорость тарифа мб/c
    price, option, equipment, period: связанные таблицы
    """
    title = models.CharField(max_length=128, verbose_name='Название тарифа')
    price = models.IntegerField(verbose_name='Стоимость месячной подписки', null=True)
    is_on_main = models.BooleanField(verbose_name='Отображение', default=True)
    option = models.ForeignKey(
        PlansOption,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Опция')
    equipment = models.ForeignKey(
        PlansEquipment,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Оборудование')
    period = models.ForeignKey(
        PlansPeriod,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Период')
    speed = models.ForeignKey(
        PlansSpeed,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Скорость интернета')
    class Meta:
        verbose_name = 'Описание тарифа'
        verbose_name_plural = 'Описание тарифов'
        ordering = ('price',)

    def __str__(self):
        return self.title




