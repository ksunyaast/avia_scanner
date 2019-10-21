from django import forms

from .widgets import AjaxInputWidget
from .models import City
from .widgets import XDSoftDateTimePickerInput


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    departure_city = forms.CharField(
        widget=AjaxInputWidget('api/city_ajax'),
        label='Город отправления:'
    )

    choices = [(0, '--------')]
    city_list = City.objects.all().order_by('name').values_list('id', 'name')
    choices.extend(city_list)
    arrival_city = forms.CharField(
        widget=forms.Select(
            choices=choices,
            attrs={'class': 'inline right-margin'}
        ),
        label='Город прибытия:'
    )
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(),
        label='Дата:'
    )

