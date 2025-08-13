from rest_framework import serializers
from ..models.students import Student
from ..models.disciplinary_records import DisciplinaryRecord
from .student_serializers import StudentSerializer
from users.models import CustomUser
from .users_serializers import CustomUserSerializer


class DisciplinaryRecordSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    reported_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    class Meta:
        model = DisciplinaryRecord
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customize representation to include detailed patient information.
        """
        representation = super().to_representation(instance)
        # Replace `patient` ID with full serialized data
        representation['student'] = StudentSerializer(instance.student).data
        representation['reported_by'] = CustomUserSerializer(instance.reported_by).data
        return representation