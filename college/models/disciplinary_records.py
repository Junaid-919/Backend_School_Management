from django.db import models
from .students import Student
from users.models import CustomUser  # import your custom user model


class DisciplinaryRecord(models.Model):
    severity_choices = [('minor', 'minor'), ('major', 'major'), ('severe', 'severe')]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="disciplinary")
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    incident_date = models.DateField()
    description = models.TextField()
    action_taken = models.TextField()
    severity = models.TextField(choices=severity_choices)
    remarks = models.TextField()