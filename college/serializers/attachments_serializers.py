from rest_framework import serializers
from ..models.attachments import Attachment
from django.conf import settings

class AttachmentSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized
    # patient = PatientSerializer()
    class Meta:
        model = Attachment
        fields = '__all__'
        # fields = ['patient', 'date_of_appointment','doctor_name', 'reason_for_appointment']
