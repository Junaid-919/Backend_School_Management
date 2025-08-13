from django.db import models
from .subjects import Subject
from .exam_incharge import ExamIncharge
from .exam_invigilator import ExamInvigilator

class Exam(models.Model):
    exam_number = models.TextField()
    exam_type = models.TextField()
    exam_date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_incharge = models.ForeignKey(ExamIncharge, on_delete=models.CASCADE, null=True, blank=True, related_name="Exam")
    exam_invigilator = models.ForeignKey(ExamInvigilator, on_delete=models.CASCADE, null=True, blank=True)