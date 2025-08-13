from rest_framework import serializers
from ..models.raise_leave import Raiseleave
from ..models.students import Student
from ..models.teachers import Teacher
from .student_serializers import StudentSerializer
from .teacher_serializers import TeacherSerializer
from users.models import CustomUser
from .users_serializers import CustomUserSerializer



class RaiseleaveSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    class Meta:
        model = Raiseleave
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customize representation to include detailed patient information.
        """
        representation = super().to_representation(instance)
        # Replace `patient` ID with full serialized data
        representation['user'] = CustomUserSerializer(instance.user).data
        return representation