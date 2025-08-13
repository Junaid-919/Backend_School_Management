from django.db import models


class ExamIncharge(models.Model):
    name = models.TextField()
    age = models.BigIntegerField()
    gender = models.TextField()
    contact = models.TextField()
    qualification = models.TextField()
    employee = models.TextField()