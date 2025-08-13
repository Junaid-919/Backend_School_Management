from django.db import models

# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)  # e.g., "BSc Computer Science"
    code = models.CharField(max_length=20, unique=True)  # e.g., "BSC-CS"
    duration_years = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.name