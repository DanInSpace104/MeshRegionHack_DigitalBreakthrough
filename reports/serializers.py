from rest_framework import routers, serializers, viewsets
from .models import Bank, Company, Account, Currency


class CompanySerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Account
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'
