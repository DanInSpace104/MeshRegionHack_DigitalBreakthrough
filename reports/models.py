from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class CompanyInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.company)


class Bank(models.Model):
    name = models.CharField(max_length=127)
    pass
    # def __str__(self):
    #     return self.infos.get()


class BankInfo(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='infos')
    bik = models.IntegerField(unique=True)
    creation_time = models.DateTimeField(auto_now=True)

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


class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)

    RUB = 'RUB'
    USD = 'USD'
    CURRENCY_CHOISES = ((RUB, 'rub'), (USD, 'usd'))
    currency = models.CharField(max_length=15, choices=CURRENCY_CHOISES)
