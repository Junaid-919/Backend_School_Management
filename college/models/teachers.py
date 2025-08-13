from django.db import models
from .grades import Grade

class Teacher(models.Model):
    teacher_name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='teacher', null=True, blank=True)