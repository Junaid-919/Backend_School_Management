from rest_framework import serializers
from ..models.fee_details import Fee_details
from ..models.students import Student
from ..models.teachers import Teacher
from .student_serializers import StudentSerializer
from .teacher_serializers import TeacherSerializer

class FeedetailSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    class Meta:
        model = Fee_details
        fields = '__all__'


    def to_representation(self, instance):
        """
        Customize representation to include detailed patient information.
        """
        representation = super().to_representation(instance)
        # Replace `patient` ID with full serialized data
        representation['student'] = StudentSerializer(instance.student).data
        representation['teacher'] = TeacherSerializer(instance.teacher).data
        return representation