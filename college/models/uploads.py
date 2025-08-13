from django.db import models

class Upload(models.Model):
    FILE_CHOICES = [('Materials', 'Materials'), ('pqp', 'pqp'), ('Notes', 'Notes'),]
    uploaded_by = models.TextField()
    upload_type = models.TextField(choices=FILE_CHOICES)