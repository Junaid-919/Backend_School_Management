from rest_framework import serializers
from ..models.student_marks import Student_marks
from .student_serializers import StudentSerializer
from ..models.students import Student
from ..models.teachers import Teacher
from ..models.exams import Exam
from .teacher_serializers import TeacherSerializer
from .exam_serializers import ExamSerializer

class StudentMarksSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())
    class Meta:
        model = Student_marks
        fields = '__all__'


    def to_representation(self, instance):
        """
        Customize representation to include detailed patient information.
        """
        representation = super().to_representation(instance)
        # Replace `patient` ID with full serialized data
        representation['student'] = StudentSerializer(instance.student).data
        representation['teacher'] = TeacherSerializer(instance.teacher).data
        representation['exam'] = ExamSerializer(instance.exam).data
        return representation