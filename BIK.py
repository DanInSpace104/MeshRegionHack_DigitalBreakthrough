import requests
import xml.etree.ElementTree as et
from lxml import etree
import os

import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mrh.settings'
django.setup()
from reports.models import Bank  # Записываем в эту таблицу
from reports.models import BankInfo  # Записываем в эту таблицу
from reports.models import Report
from reports.models import Account
from django.db.utils import IntegrityError


tree = et.parse('list_bik.xml')
xml = tree.getroot()


for i in range(len(xml)):
    bik = xml[i].attrib['BIC']
    for j in xml[i]:
        if str(j.tag) == '{urn:cbr-ru:ed:v2.0}ParticipantInfo':
            name = j.attrib['NameP']
            date_reg = j.attrib['DateIn']
    bank = Bank(name=name)
    try:
        bank.save()
    except IntegrityError:
        pass
    else:
        BankInfo(bank=bank, bik=bik, name=name).save()