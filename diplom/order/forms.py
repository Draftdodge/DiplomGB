
from django import forms


class SearchOrderForm(forms.Form):
    phone = forms.CharField(label='Введите номер телефона в формате +7XXXXXXXXXX', max_length=12)
