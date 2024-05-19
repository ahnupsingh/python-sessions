from rest_framework import serializers
from ramailo.models.company import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['idx', 'name']