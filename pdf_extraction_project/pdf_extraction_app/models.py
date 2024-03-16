from django.db import models

class ExtractedData(models.Model):
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
