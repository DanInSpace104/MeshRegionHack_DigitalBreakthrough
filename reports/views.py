from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import viewsets, permissions
import os
from .models import Company, Account, Bank, Currency, Report
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import mimetypes
from create_report import create_report
import json
from .serializers import (
    CompanySerializer,
    BankSerializer,
    AccountSerializer,
    SuperAccountSerializer,
    CurrencySerializer,
    BankBikSerializer,
    ReportSerializer,
)

def accts(request):
    return render(request, 'reports/accts.html')

def createacct(request):
    return render(request, 'reports/createacct.html')

def selectorg(request):
    return render(request, 'reports/selectorg.html')

def adminpanel(request):
    return render(request, 'reports/adminpanel.html')


class CompanysViewSet(viewsets.ModelViewSet):
    model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportsListView(generics.ListAPIView):
    model = Report
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        data = json.loads(data['data'])
        # print("data", json.loads(data['data']))
        excel_file_name = create_report(data)
        print("excel_file_name", excel_file_name)
        # excel_file_name = ''
        return HttpResponse(excel_file_name)


@api_view(('POST',))
@renderer_classes([JSONRenderer])
def change_accounts(request):
    data = request.POST
    for id, bal in data.items():
        id = int(id)
        bal = int(bal)
        acc = Account.objects.get(pk=id)
        if acc.balance != bal:
            acc.balance = bal
            acc.save()
            print(id)
    return Response(status=200)


def choose_company(request):
    data = request.POST.get('company_id')
    # for id, bal in d
    response = HttpResponse()
    response.set_cookie('company_id', data)
    return response


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
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bank.objects.all()


class AccountsViewSet(viewsets.ModelViewSet):
    model = Account
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]


class AccountsViewSet(viewsets.ModelViewSet):
    model = Account
    serializer_class = SuperAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        companys = Company.objects.filter(users__pk=user.pk)
        return Account.objects.filter(company__in=companys)
