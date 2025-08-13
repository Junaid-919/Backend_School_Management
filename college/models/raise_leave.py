from django.db import models
from users.models import CustomUser 


class Raiseleave(models.Model):
    # Step 1: Fields required for GenericForeignKey

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    reason_for_leave = models.TextField()
    date_of_leave = models.DateField()
    return_date = models.DateField()
    instance_id = models.BigIntegerField(null=True, blank=True)

