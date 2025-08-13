from django.db import models
from .uploads import Upload

class Attachment(models.Model):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
