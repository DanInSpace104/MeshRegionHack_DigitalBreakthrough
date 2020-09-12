from django.db import models


class Company(models.Model):
    name = models.TextField(max_length=127)


class Bank(models.Model):
    name = models.TextField(max_length=127)


class BankInfo(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bik = models.IntegerField(unique=True)


class Report(models.Model):
    bank_info = models.ForeignKey(BankInfo, on_delete=models.PROTECT)


class ReportInfo(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
