from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .fee_term import FeeTerm



# Fee Components under a FeeTerm
class FeeComponent(models.Model):
    fee_term = models.ForeignKey(FeeTerm, on_delete=models.CASCADE, related_name='components')
    name = models.CharField(max_length=100)  # e.g., "Tuition Fee", "Admission Fee"
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.fee_term.name}"