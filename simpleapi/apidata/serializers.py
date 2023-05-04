from rest_framework import serializers
from .models import *

class DataSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Data
        fields = '__all__'
    