from django.db import models


class College(models.Model):
    
    college_name = models.TextField()
    address = models.TextField()
    phone = models.BigIntegerField()
    