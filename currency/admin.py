from django.contrib import admin
from .models import RatesData


class RatesDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'usd', 'czk', 'eur', 'pln', 'date']
       
admin.site.register(RatesData, RatesDataAdmin)

