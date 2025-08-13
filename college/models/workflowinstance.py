from django.db import models
from django.utils import timezone
from .workflowdesign import WorkflowDesign
from .workflowsteps import WorkflowStep



class WorkflowInstance(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    workflow_design = models.ForeignKey(WorkflowDesign, on_delete=models.CASCADE, related_name='instances')
    current_step = models.ForeignKey(WorkflowStep, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.status}"