from django.shortcuts import render
from currency.models import RatesData
import datetime


def mainview(request):
    datetoday = datetime.datetime.now()
    currency = RatesData.objects.get(id='1')
    return render(request, 'currency/main.html', {
        'currency':currency,
        'datetoday':datetoday,
    })






