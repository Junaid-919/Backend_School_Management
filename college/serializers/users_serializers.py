from rest_framework import serializers
from users.models import CustomUser
from ..models.grades import Grade
from .grades_serializers import GradeSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    grade = serializers.PrimaryKeyRelatedField(queryset=Grade.objects.all())
    class Meta:
        model = CustomUser
        fields = '__all__'  # or list specific fields

    def to_representation(self, instance):
        """
        Customize representation to include detailed patient information.
        """
        representation = super().to_representation(instance)
        # Replace `patient` ID with full serialized data
        representation['grade'] = GradeSerializer(instance.grade).data
        return representation