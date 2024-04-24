from rest_framework import serializers
from .models import Product
from.models import Company
class ProductSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CompanySerializaer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
