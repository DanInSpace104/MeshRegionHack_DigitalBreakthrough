import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mrh.settings'
import django
django.setup()
#####
from reports.models import Company
print(Company.objects.all())
