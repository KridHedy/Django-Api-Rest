from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'gender', 'company', 'city', 'title')