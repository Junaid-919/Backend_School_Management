# from django.db import models


# class Feestructure(models.Model):
#     PAYMENT_CHOICES = [('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annually', 'Annually'),]
#     SEAT_CHOICES = [('Free_seat', 'Free_seat'), ('Management_quota', 'Management_quota'), ('Government_funded', 'Government_funded'),]
    
#     seat_type = models.TextField(choices=SEAT_CHOICES)
#     payment_method = models.TextField(choices=PAYMENT_CHOICES)
#     fee_amount = models.BigIntegerField()
#     instance_id = models.BigIntegerField(null=True, blank=True)

from django.db import models
from django.core.validators import MinValueValidator
from .course import Course


# Fee Structure linked to Course
class FeeStructure(models.Model):
    ADMISSION_TYPES = [
        ('Regular', 'Regular'),
        ('Lateral_Entry', 'Lateral_Entry'),
        ('Management_Quota', 'Management_Quota'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='fee_structures')
    admission_type = models.CharField(max_length=20, choices=ADMISSION_TYPES)
    total_fee_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    academic_year = models.CharField(max_length=9)  # e.g., "2025-2026"
    instance_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('course', 'admission_type', 'academic_year')

    def __str__(self):
        return f"{self.course.name} - {self.admission_type} - {self.academic_year}"