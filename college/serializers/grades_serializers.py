from rest_framework import serializers
from ..models.grades import Grade


class GradeSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized
    
    class Meta:
        model = Grade
        fields = '__all__'