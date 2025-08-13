from django.db import models
from .students import Student

class ActionRequired(models.Model):
    ACTION_TYPES = [
        ('TC_APPROVAL', 'Pending TC Approval'),
        ('FEE_DUE', 'Fee Due'),
        ('DISCIPLINARY', 'Disciplinary Review'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES)
    details = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.enrollment_number} - {self.get_action_type_display()}"