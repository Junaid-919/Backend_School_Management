from rest_framework import serializers
from ..models.exam_invigilator import ExamInvigilator

class ExamInvigilatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamInvigilator
        fields = '__all__'