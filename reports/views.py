from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets, permissions
from .models import Company, Account, Bank, Currency
from .serializers import CompanySerializer, BankSerializer, AccountSerializer, CurrencySerializer


def index(request):
    return render(request, 'reports/base.html')


def create_report(request):
    return render(request, 'asht')


class CompanysViewSet(viewsets.ModelViewSet):
    model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class BanksViewSet(viewsets.ModelViewSet):
    model = Bank
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountsViewSet(viewsets.ModelViewSet):
    model = Account
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrencyViewSet(viewsets.ModelViewSet):
    model = Currency
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
