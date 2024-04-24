from django.shortcuts import render, redirect
from parkings import models
from .forms import SearchOrderForm

def order_search(request):
    """Отображение заказов пользователя.

    :phone: номер телефона, по которому проводится выборка
    """

    if request.method == 'POST':
        message = 'Результаты поиска'
        form_ = SearchOrderForm(request.POST)
        if form_.is_valid():
            phone = form_.cleaned_data['phone']
            clients = models.Client.objects.filter(phone=phone)
            if not clients:
                message = 'Клиент не найден'
            return render(request, 'order_search.html', {'form': form_, 'clients': clients, 'message': message})
    else:
        form_ = SearchOrderForm()
        message = 'Заполните форму'
    return render(request, 'order_search.html', {'form': form_, 'message': message})

