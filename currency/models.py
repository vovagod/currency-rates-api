from django.db import models
import datetime

# Create your models here.
class RatesData(models.Model):
    usd = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="USD")
    czk = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="CZK")
    eur = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="EUR")
    pln = models.DecimalField(max_digits=5, decimal_places=2, default='1', verbose_name="PLN")
    date = models.DateTimeField(auto_now = True)
   
