from rest_framework import routers, serializers, viewsets
from .models import Bank, Company, Account, Currency


class CompanySerializer(serializers.ModelSerializer):
    inn = serializers.ReadOnlyField(source='last_info.inn')
    kpp = serializers.ReadOnlyField(source='last_info.kpp')
    company_type = serializers.ReadOnlyField(source='last_info.company_type')

    class Meta:
        model = Company
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class BankBikSerializer(serializers.ModelSerializer):
    model = Bank
    bik = serializers.ReadOnlyField(source='last_info.bik')

    class Meta:
        model = Bank
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    currency_name = serializers.ReadOnlyField(source='currency.name')
    bank_name = serializers.ReadOnlyField(source='bank.name')
    bik = serializers.ReadOnlyField(source='bank.last_info.bik')
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Account
        fields = '__all__'


class SuperAccountSerializer(serializers.ModelSerializer):
    currency_code = serializers.ReadOnlyField(source='currency.code')
    bank_name = serializers.ReadOnlyField(source='bank.name')
    bik = serializers.ReadOnlyField(source='bank.last_info.bik')
    kpp = serializers.ReadOnlyField(source='bank.last_info.kpp')
    inn = serializers.ReadOnlyField(source='bank.last_info.inn')
    company_name = serializers.ReadOnlyField(source='company.name')
    gofl = serializers.ReadOnlyField(source='company.last_info.company_type')

    class Meta:
        model = Account
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
