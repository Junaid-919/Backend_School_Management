from rest_framework import serializers
from ..models.workflowsteps import WorkflowStep

class WorkflowStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowStep
        fields = '__all__'