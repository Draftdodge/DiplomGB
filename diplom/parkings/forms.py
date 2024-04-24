from datetime import datetime

from django import forms



class ParkingsForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100)
    phone = forms.CharField(label='Телефон(+7XXXXXXXXXX)', max_length=20)
    car_number = forms.CharField(label='Номер авто(X123XXYYY)',max_length=9)
    start_access_date = forms.DateField(label='Дата начала аренды', widget=forms.DateInput(attrs={'type': 'date','class':'datepicker', 'value': datetime.now().strftime("%Y-%m-%d")}))
    access_delta = forms.DateField(label='Дата окончания аренды', widget=forms.DateInput(attrs={'type': 'date','class':'datepicker', 'value': datetime.now().strftime("%Y-%m-%d")}))
    description = forms.CharField(label='Примечание', widget=forms.Textarea, max_length=1000, required=False)

