from rest_framework import serializers
from ..models.college import College


class CollegeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = College
        fields = '__all__'