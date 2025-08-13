from rest_framework import serializers
from .student_serializers import StudentSerializer
from ..models.actionrequired import ActionRequired
from ..models.students import Student


class ActionRequiredSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    enrollment_number = serializers.CharField(write_only=True)

    class Meta:
        model = ActionRequired
        fields = ['id', 'student', 'enrollment_number', 'action_type', 'details', 'due_date']

    def validate_enrollment_number(self, value):
        try:
            Student.objects.get(enrollment_number=value)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Student with this enrollment number does not exist.")
        return value

    def create(self, validated_data):
        enrollment_number = validated_data.pop('enrollment_number')
        student = Student.objects.get(enrollment_number=enrollment_number)
        action = ActionRequired.objects.create(student=student, **validated_data)
        return action

    def update(self, instance, validated_data):
        if 'enrollment_number' in validated_data:
            enrollment_number = validated_data.pop('enrollment_number')
            instance.student = Student.objects.get(enrollment_number=enrollment_number)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance