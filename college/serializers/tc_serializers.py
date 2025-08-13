from rest_framework import serializers
from ..models.students import Student
from ..models.transfer_certificate import TransferCertificate
from .student_serializers import StudentSerializer


class TCSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    class Meta:
        model = TransferCertificate
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customize representation to include detailed patient information.
        """
        representation = super().to_representation(instance)
        # Replace `patient` ID with full serialized data
        representation['student'] = StudentSerializer(instance.student).data
        return representation