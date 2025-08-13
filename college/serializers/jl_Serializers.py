from rest_framework import serializers
from ..models.junior_lecturer import Juniorlecturer

class Juniorlecturer_serializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized



    class Meta:
        model = Juniorlecturer
        fields = '__all__'