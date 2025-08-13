from rest_framework import serializers
from ..models.subjects import Subject

class SubjectSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized

    class Meta:
        model = Subject
        fields = '__all__'