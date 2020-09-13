import django
import datetime
from openpyxl import Workbook
import os
import xml.etree.ElementTree as ET



def create_report(file_format):
    '''
    Функция создания отчета, для дальнейшего вывода или отправки
    format - xls, xml, xlsx
    '''
    # # Берем данные из этих сущностей
    # from reports.models import Company
    # from reports.models import CompanyInfo
    # from reports.models import Bank
    # from reports.models import BankInfo
    # from reports.models import Report
    # from reports.models import ReportInfo
    # from reports.models import Currency
    # from reports.models import Account
    # os.environ['DJANGO_SETTINGS_MODULE'] = 'mrh.settings'
    # django.setup()

    # Берем из БД все нужные данные для отчета
    # print(Currency.objects.all().values("code"))
    # company_id = Company.objects.filter().values("ID")
    # INN = Company.objects.filter().values("INN")
    # KPP = Company.objects.filter().values("KPP")
    # ...
    
    

    now = datetime.datetime.now()  # Текущая дата
    now_format = now.strftime("%Y-%m-%d_%H-%M")
    now_format = now.strftime("%Y-%m-%d")
    a = [1, 2, 3]
    # print(now_format)
    if file_format == 'xls':
        directory = os.path.abspath(os.curdir)  # Директория
    #     # Создаем подключение
    #     wb = Workbook()
    #     ws = wb.active

    #     # Назначаем данные нужной ячейке
    #     ws['A1'] = '42'
    #     # ws['B2'] = 24
    #     # ws.append([1, 2, 3])
    #     # ws['A2'] = datetime.datetime.now()

    #     # Save the file
    #     ws.merge_cells('C2:C4')
    #     wb.save(f"{now_format}.xml")
    elif file_format == 'xml':
        data = ET.Element('Info')

        # Создаются блоки
        organ_block = ET.SubElement(data, 'Organization')
        bank_block = ET.SubElement(data, 'Bank')
        score_block = ET.SubElement(data, 'Score')

        # Создаем элементы
        ID_el = ET.SubElement(organ_block, 'ID')
        INN_el = ET.SubElement(organ_block, 'INN')
        KPP_el = ET.SubElement(organ_block, 'KPP')
        go_fl_el = ET.SubElement(organ_block, 'go-fl')

        bik_el = ET.SubElement(bank_block, 'bik')
        bank_name_el = ET.SubElement(bank_block, 'bank_name')

        # Наполняем элементы
        ID_el.text = "902"
        INN_el.text = "431320498712942"
        KPP_el.text = "414126213"
        go_fl_el.text = "go"

        bik_el.text = "532423432"
        bank_name_el.text = "ВТБ Банк"
        # bank_name_el.text = "ВТБ Банк"

        # Для договоров, обходим в цикле, их несколько
        for i in a:
            date = ET.SubElement(score_block, f'contract_{i}')
            date.text = "10.12.2020"
            date = ET.SubElement(score_block, f'contract_{i}')
            date.text = "10.12.2020"

        # Converting the xml data to byte object,
        # for allowing flushing data to file
        # stream
        b_xml = ET.tostring(data)

        # Opening a file under the name `items2.xml`,
        # with operation mode `wb` (write + binary)
        with open(f"{now_format}.xml", "wb") as f:
            f.write(b_xml)


create_report('xml')
