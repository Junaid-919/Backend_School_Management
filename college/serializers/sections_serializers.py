from rest_framework import serializers
from ..models.sections import Section


class SectionSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized
    
    class Meta:
        model = Section
        fields = '__all__'