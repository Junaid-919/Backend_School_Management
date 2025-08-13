from rest_framework import serializers
from ..models.workflowinstancesteps import WorkflowInstanceStep
from .workflowstep_serializers import WorkflowStepSerializer




class WorkflowInstanceStepSerializer(serializers.ModelSerializer):
    workflow_step = WorkflowStepSerializer()

    class Meta:
        model = WorkflowInstanceStep
        fields = '__all__'