from django.db import models
from .students import Student
from .junior_lecturer import Juniorlecturer
from .teachers import Teacher
from .exams import Exam


class Student_marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='Student_marks')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='Student_marks')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,related_name='Student_marks', null=True, blank=True)
    marks = models.BigIntegerField()
