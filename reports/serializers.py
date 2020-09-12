from rest_framework import routers, serializers, viewsets
from .models import Company


class CompanySerializer(serializers.BaseSerializer):
    class Meta:
        model = Company
