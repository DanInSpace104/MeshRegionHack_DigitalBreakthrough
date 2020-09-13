import django
import requests
import xml.etree.ElementTree as et
from lxml import etree
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mrh.settings'
django.setup()
from reports.models import Currency  # Записываем в эту таблицу

print(Currency.objects.all().values("code"))
req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
if req.status_code == 200: # Если получили нормальный ответ
    print(req.status_code)
    xml = req.text
    xml = et.XML(xml)

    for i in range(len(xml)):
        for j in xml[i]:
            # print(j.tag)
            # print(j.text)
            if j.tag == 'CharCode':
                char_code = j.text
                # print('CharCode: ', j.text)
            elif j.tag == 'Nominal':
                nominal = int(j.text) # Делаем переменную, что бы потом посчитать курс за 1 валюту
            elif j.tag == 'Name':
                name = j.text
                # print('Name: ', j.text, end=' ')
            elif j.tag == 'Value':
                value = f'{float(j.text.replace(",", "."))/nominal:.2f}'
                value = float(value)
                # print(f'Value: {value}')

        # Create new velue and update
        try:
            Currency(name=name, code=char_code,
                    course=value).save()
            print('Данные созданы')

        except django.db.utils.IntegrityError:
            Currency.objects.filter(code=char_code).update(course=value)
            print('Данные обновлены')

else:
    print('Доступ не получен: ', req.status_code)
