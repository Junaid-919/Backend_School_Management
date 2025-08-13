from rest_framework import serializers
from ..models.principal import Principal

class PrincipalSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized


    class Meta:
        model = Principal
        fields = '__all__'

