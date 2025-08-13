from rest_framework import serializers
from ..models.exam_incharge import ExamIncharge

class ExamInchargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamIncharge
        fields = '__all__'