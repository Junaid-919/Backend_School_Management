from django.db import models
from .teachers import Teacher
from .students import Student

class Fee_details(models.Model):
    reciept_number = models.TextField()
    payment_date = models.DateField()
    total_fee = models.BigIntegerField()
    payment_amount = models.BigIntegerField()
    total_due = models.BigIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='Fee_details')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='Fee_details')