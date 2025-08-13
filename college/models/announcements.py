from django.db import models

class Announcement(models.Model):
    announcement_creator = models.TextField()
    announcement_headline = models.TextField()
    announcement_description = models.TextField()
