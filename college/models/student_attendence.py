from django.db import models
from .students import Student
from .teachers import Teacher


class Student_attendence(models.Model):
    ATTENDENCE_CHOICES = [('present', 'present'), ('absent', 'absent'), ('leave', 'leave')]
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='Student_attendence')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='Student_attendence')
    date = models.DateField(auto_now_add=True)
    attendance = models.TextField(choices=ATTENDENCE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'date')  # Ensures uniqueness
        verbose_name = 'Student Attendance'
        verbose_name_plural = 'Student Attendances'