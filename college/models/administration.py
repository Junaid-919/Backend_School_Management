from django.db import models

class Administration(models.Model):
    admin_name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()