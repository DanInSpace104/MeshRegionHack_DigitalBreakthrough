from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView
from rest_framework import generics
from rest_framework import viewsets, permissions
from .models import Company, Account, Bank, Currency
from .serializers import (
    CompanySerializer,
    BankSerializer,
    AccountSerializer,
    CurrencySerializer,
    BankBikSerializer,
)

def accts(request):
    return render(request, 'reports/accts.html')

def createacct(request):
    return render(request, 'reports/createacct.html')


class CompanysViewSet(viewsets.ModelViewSet):
    model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanysViewSet(viewsets.ModelViewSet):
    model = Company
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return get_list_or_404(Company, users__pk=self.request.user.pk)


class BanksViewSet(viewsets.ModelViewSet):
    model = Bank
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankBiksViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BankBikSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Bank.objects.all()


class AccountsViewSet(viewsets.ModelViewSet):
    model = Account
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        companys = Company.objects.filter(users__pk=user.pk)
        return Account.objects.filter(company__in=companys)


class AccountsByCompList(generics.ListAPIView):
    model = Account
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        comp_id = self.kwargs['company_id']
        company = get_object_or_404(Company.objects.filter(users__pk=user.pk), pk=comp_id)
        return Account.objects.filter(company=company)


class CurrencyViewSet(viewsets.ModelViewSet):
    model = Currency
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = [permissions.IsAuthenticated]
