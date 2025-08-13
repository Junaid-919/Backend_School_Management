from django.db import models
from .teachers import Teacher
from users.models import CustomUser  # import your custom user model


class Daily_login(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    login_date = models.DateField()
    login_time = models.TimeField()
    logout_time = models.TimeField(null=True, blank=True)