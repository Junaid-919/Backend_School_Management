from rest_framework import serializers
from ..models.senior_lecturer import Seniorlecturer

class Seniorlecturer_serializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized



    class Meta:
        model = Seniorlecturer
        fields = '__all__'

