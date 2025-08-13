from rest_framework import serializers
from ..models.exams import Exam
from ..models.subjects import Subject
from ..models.exam_incharge import ExamIncharge
from ..models.exam_invigilator import ExamInvigilator
from .subjects_serializers import SubjectSerializer
from .exam_incharge_serializers import ExamInchargeSerializer
from .exam_invigilator_serializers import ExamInvigilatorSerializer

class ExamSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    exam_incharge = serializers.PrimaryKeyRelatedField(queryset=ExamIncharge.objects.all())
    exam_invigilator = serializers.PrimaryKeyRelatedField(queryset=ExamInvigilator.objects.all())
    class Meta:
        model = Exam
        fields = '__all__'


    def to_representation(self, instance):
        """
        Customize representation to include detailed patient information.
        """
        representation = super().to_representation(instance)
        # Replace `patient` ID with full serialized data
        representation['subject'] = SubjectSerializer(instance.subject).data
        representation['exam_incharge'] = ExamInchargeSerializer(instance.exam_incharge).data
        representation['exam_invigilator'] = ExamInvigilatorSerializer(instance.exam_invigilator).data
        return representation