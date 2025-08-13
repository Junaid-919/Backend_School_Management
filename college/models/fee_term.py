from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .fee_structure import FeeStructure


# Fee Terms under a FeeStructure
class FeeTerm(models.Model):
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE, related_name='terms')
    name = models.CharField(max_length=50)  # e.g., "Term 1"
    start_date = models.DateField()
    end_date = models.DateField()
    term_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} ({self.fee_structure})"

    def clean(self):
        if self.fee_structure:
            other_terms = self.fee_structure.terms.exclude(id=self.id)
            total = sum(term.term_amount for term in other_terms) + self.term_amount
            if total > self.fee_structure.total_fee_amount:
                raise ValidationError(f"Total of all terms exceeds fee structure total ({self.fee_structure.total_fee_amount}).")
