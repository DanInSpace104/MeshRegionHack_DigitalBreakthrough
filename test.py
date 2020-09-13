import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mrh.settings'
import django
django.setup()
#####
from reports.models import Company
from reports.models import Bank

print(Company.objects.all())
print(Bank.objects.all())
