from django.db import models


class Juniorlecturer(models.Model):
    lecturer_name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()