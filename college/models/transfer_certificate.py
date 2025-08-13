from django.db import models
from .students import Student
from users.models import CustomUser  # import your custom user model


class TransferCertificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='tc')
    tc_number = models.TextField()
    issue_date = models.DateField()
    reason_for_leaving = models.TextField()
    last_class_attended = models.DateField()
    conduct = models.TextField()
    remarks = models.TextField()
    issued_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)