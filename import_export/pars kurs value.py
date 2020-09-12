import requests
import xml.etree.ElementTree as et
from lxml import etree

req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
if req.status_code == 200: # Если получили нормальный ответ
    print(req.status_code)
    xml = req.text
    xml = et.XML(xml)

    for i in range(len(xml)):
        print('------')
        for j in xml[i]:
            # print(j.tag)
            # print(j.text)
            if j.tag == 'CharCode':
                print('CharCode: ', j.text)
            elif j.tag == 'Nominal':
                nominal = int(j.text) # Делаем переменную, что бы потом посчитать курс за 1 валюту
            elif j.tag == 'Name':
                print('Name: ', j.text, end=' ')
            elif j.tag == 'Value':
                print(f'Value {float(j.text.replace(",", "."))/nominal:.2f}')
else:
    print('Доступ не получен: ', req.status_code)
