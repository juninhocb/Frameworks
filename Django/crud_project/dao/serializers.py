from rest_framework import serializers
from .models import Person, Office

class OfficeSerializerToJson(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

class PersonSerializerToJson(serializers.ModelSerializer):
    idOffice = OfficeSerializerToJson()
    
    class Meta:
        model = Person
        fields = '__all__'