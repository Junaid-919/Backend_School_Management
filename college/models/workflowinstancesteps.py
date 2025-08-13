from django.db import models
from django.utils import timezone
from .workflowinstance import WorkflowInstance
from .workflowsteps import WorkflowStep

class WorkflowInstanceStep(models.Model):
    workflow_instance = models.ForeignKey(WorkflowInstance, on_delete=models.CASCADE, related_name='instance_steps')
    workflow_step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    completed_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.workflow_instance.name} -> {self.workflow_step.name} ({'Done' if self.completed else 'Pending'})"