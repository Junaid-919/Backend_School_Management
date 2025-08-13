from django.db import models


class Principal(models.Model):
    principal_name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()