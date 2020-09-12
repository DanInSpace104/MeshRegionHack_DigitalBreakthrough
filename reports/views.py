from django.shortcuts import render
from django.views.generic import ListView
from .models import Company


def index(request):
    return render(request, 'reports/base.html')


def create_report(request):
    return render(request, 'asht')


class CompanysViewSet(viewsets.):
    model = Company
    template_name = 'reports/companys.html'
