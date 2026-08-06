from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Tour(models.Model):
    title = models.CharField(max_length=150,null=False,blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(Decimal("0.01"))])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
