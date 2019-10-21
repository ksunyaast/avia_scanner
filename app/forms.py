import datetime

from django import forms
from django.forms import SelectDateWidget

from .widgets import AjaxInputWidget
from .models import City
from django.utils.translation import ugettext as _
from .widgets import XDSoftDateTimePickerInput

year = datetime.date.today().year
months = {
    1:_('Январь'), 2:_('Февраль'), 3:_('Март'), 4:_('Апрель'),
    5:_('Май'), 6:_('Июнь'), 7:_('Июль'), 8:_('Август'),
    9:_('Сентябрь'), 10:_('Октябрь'), 11:_('Ноябрь'), 12:_('Декабрь')
}


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

    # не работает
    #  date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=XDSoftDateTimePickerInput(),
    #     label='Дата:'
    # )

    # работает
    date = forms.DateField(label=_('Дата:'), initial=datetime.date.today,
                           widget=SelectDateWidget(years=range(year, year+100, +1), months=months))

