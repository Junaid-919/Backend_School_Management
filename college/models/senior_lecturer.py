from django.db import models

class Seniorlecturer(models.Model):
    lecturer_name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()