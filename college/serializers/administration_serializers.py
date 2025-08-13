from rest_framework import serializers
from ..models.administration import Administration

class AdministrationSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized


    class Meta:
        model = Administration
        fields = '__all__'