from rest_framework import serializers
from ..models.workflowdesign import WorkflowDesign
from .workflowstep_serializers import WorkflowStepSerializer



class WorkflowDesignSerializer(serializers.ModelSerializer):
    steps = WorkflowStepSerializer(many=True, read_only=True)

    class Meta:
        model = WorkflowDesign
        fields = '__all__'