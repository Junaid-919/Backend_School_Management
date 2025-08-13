from django.contrib.auth.models import AbstractUser
from django.db import models
from college.models.grades import Grade

class RoleChoices(models.TextChoices):
    JL = 'JL', 'Junior Lecturer'
    SL = 'SL', 'Senior Lecturer'
    PRINCIPAL = 'PR', 'Principal'
    ADMIN = 'AD', 'Admin'

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=2,
        choices=RoleChoices.choices,
        default=RoleChoices.JL
    )

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    is_active_faculty = models.BooleanField(default=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='customuser', null=True, blank=True)

    # Common to JL / SL / Principal
    subject_specialization = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    designation = models.ForeignKey(Designation, null=True, blank=True, on_delete=models.SET_NULL)
    employee_id = models.CharField(max_length=20, unique=True)
    date_of_joining = models.DateField(null=True, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    reporting_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subordinates')

    # Admin-only
    access_level = models.IntegerField(blank=True, null=True)
    system_notes = models.TextField(blank=True)
    can_impersonate_users = models.BooleanField(default=False)

    # Principal-only
    tenure_start = models.DateField(blank=True, null=True)
    tenure_end = models.DateField(blank=True, null=True)
    achievements = models.TextField(blank=True)
    office_contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username