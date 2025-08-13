from rest_framework import serializers
from ..models.workflowinstance import WorkflowInstance
from .workflowdesign_serializers import WorkflowDesignSerializer
from .workflowstep_serializers import WorkflowStepSerializer




class WorkflowInstanceDetailSerializer(serializers.ModelSerializer):
    workflow_design = WorkflowDesignSerializer()
    current_step = WorkflowStepSerializer()

    class Meta:
        model = WorkflowInstance
        fields = '__all__'