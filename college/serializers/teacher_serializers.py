from rest_framework import serializers
from ..models.teachers import Teacher
from ..models.grades import Grade
from .grades_serializers import GradeSerializer

class TeacherSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized
    grade = serializers.PrimaryKeyRelatedField(queryset=Grade.objects.all())


    class Meta:
        model = Teacher
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['grade'] = GradeSerializer(instance.grade).data
        return representation