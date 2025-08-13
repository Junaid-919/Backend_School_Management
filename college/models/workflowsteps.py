from django.db import models
from .workflowdesign import WorkflowDesign

class WorkflowStep(models.Model):
    name = models.CharField(max_length=255)
    step_order = models.IntegerField()
    workflow_design = models.ForeignKey(WorkflowDesign, on_delete=models.CASCADE, related_name='steps')

    class Meta:
        ordering = ['step_order']

    def __str__(self):
        return f"{self.name} (Step {self.step_order})"