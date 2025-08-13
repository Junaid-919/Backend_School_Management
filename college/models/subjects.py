from django.db import models

class Subject(models.Model):
    subject_name = models.TextField()
    subject_code = models.TextField()
    max_marks = models.TextField()