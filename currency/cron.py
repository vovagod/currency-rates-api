import requests
from currency.models import RatesData
import datetime
from django_cron import CronJobBase, Schedule

URL='https://openexchangerates.org/api/latest.json?app_id=ba56ca3c1e0b4fc289fddfec67672a3c' # request to the service with your app_id

# a request to the service is done using django-crone
class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['03:00'] # the currency rates update time
    def __init__(self):
        self.r = requests.get(URL)

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'cron.MyCronJob'    

    def do(self):
        response = self.r.json()
        currency = response['rates']
        usd = currency['USD']
        czk = currency['CZK']
        eur = currency['EUR']
        pln = currency['PLN']
        now = datetime.datetime.now()
        RatesData.objects.filter(id='1').update(usd=usd, czk=czk, eur=eur, pln=pln, date=now) # update record in the database


        
