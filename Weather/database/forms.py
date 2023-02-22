from django import forms
from .models import CityBase
from .models import TemperatureBaseOn
from django.forms import ModelForm, NumberInput ,TextInput, TimeInput, DateInput



class CityBaseForm(ModelForm):
    class Meta:
        model = CityBase
        fields  = ['name_city']

        widgets={
            'name_city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование города'
            })
        }
class TempBaseForm(ModelForm):
    class Meta:
        model = TemperatureBaseOn
        fields  = '__all__'

class TempBaseFindForm(ModelForm):
    class Meta:
        model = TemperatureBaseOn
        fields  = ['i_city','date','t', 'temperaturedata']

class TempAddForm(ModelForm):
    class Meta:
        model = TemperatureBaseOn
        fields = ['i_city','temperaturedata','date','t']


        widgets = {
           'temperaturedata': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Температура'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата (в формате YYYY-MM-DD)'
            }),
            't': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время (в формате HH:MM)'
            }),

        }


class CityBaseEditForm(ModelForm):
    class Meta:
        model = CityBase
        fields  = ['name_city']

        widgets={
            'name_city':TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование города'
            }),
            'name_city_new': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование города'
            }),
        }