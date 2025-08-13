from django.db import models
from .course import Course
from .sections import Section
from .grades import Grade


class Student(models.Model):
    enrollment_number = models.CharField(max_length=20, unique=True)
    student_name = models.TextField()
    gender = models.TextField()
    joining_date = models.DateField()
    passout_date = models.DateField(null=True, blank=True)
    gardian_name = models.TextField()
    occupation = models.TextField(null=True, blank=True)
    phone_number = models.TextField()
    address = models.TextField()
    fee_paid = models.BigIntegerField()
    fee_due = models.BigIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='Student', null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,related_name='Student')    
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,related_name='Student')
    photo = models.FileField(upload_to='students_img/', blank=True, null=True)    