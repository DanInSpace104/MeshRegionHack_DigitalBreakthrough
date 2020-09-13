from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=127)
    users = models.ManyToManyField(User)
    INN = models.IntegerField(max_length=12)
    KPP = models.IntegerField(max_length=9)
    GO = 'ГО'
    FL = 'ФЛ'
    ACCOUNT_TYPES = (
        (GO, 'ГО'),
        (FL,'ФЛ'),
    )
    def __str__(self):
        return self.name

    @property
    def last_info(self):
        return self.infos.all().order_by('creation_time')[0]


class CompanyInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='infos')
    creation_time = models.DateTimeField(auto_now=True)
    inn = models.IntegerField(null=True)
    kpp = models.IntegerField(null=True)
    GO = 'ГО'
    FL = 'ФЛ'
    COMPANY_TYPES = (
        (GO, 'ГО'),
        (FL,'ФЛ'),
    )
    company_type = models.CharField(max_length=3, choices=COMPANY_TYPES, default=GO)



    def __str__(self):
        return str(self.company)


class Bank(models.Model):
    name = models.CharField(max_length=127, unique=True)

    @property
    def last_info(self):
        return self.infos.all().order_by('creation_time')[0]

    def __str__(self):
        return self.name


class BankInfo(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='infos')
    bik = models.IntegerField(unique=True)
    creation_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=127, default='')

    def __str__(self):
        return str(self.bank) + ' ' + str(self.creation_time)


class Report(models.Model):
    bank_info = models.ForeignKey(BankInfo, on_delete=models.PROTECT)
    company_info = models.ForeignKey(CompanyInfo, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ReportInfo(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    company_info = models.ForeignKey(CompanyInfo, on_delete=models.PROTECT)
    creation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=127)
    code = models.CharField(max_length=7, null=True, unique=True)
    course = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    CRED = 'credit'
    DEP = 'deposit'
    ACCOUNT_TYPES = (
        (DEP, 'deposit'),
        (CRED, 'credit'),
    )
    acc_type = models.CharField(max_length=15, choices=ACCOUNT_TYPES, default=DEP)
    balance = models.FloatField(default=0)
    summ = models.FloatField(default=0)
    contract_create_date = models.DateField(auto_now=True)
    contract_begin_date = models.DateField()
    comment = models.TextField(null=True)
    contract_end_date = models.DateField()
    settlement_rate = models.FloatField(default=0)
