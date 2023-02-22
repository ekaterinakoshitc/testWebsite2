from django.db import models
from django.conf import settings

# Create your models here.
class CityBase(models.Model):
    name_city = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural= 'Города'

class TemperatureBaseOn(models.Model):
    i_city  = models.ForeignKey(CityBase, on_delete = models.PROTECT,verbose_name='Город')
    temperaturedata = models.IntegerField('Температура')
    date = models.DateField('Дата')
    t = models.TimeField('Час')

    def __int__(self):
        return self.temperaturedata


    class Meta:
        verbose_name = 'Значение температуры'
        verbose_name_plural= 'Значения температур'


