from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models


class Tour(models.Model):

    MEAL_CHOICES = [
        ("breakfast", "Breakfast"),
        ("two_meals", "2 meals"),
        ("three_meals", "3 meals"),
        ("all_inclusive", "All Inclusive"),
        ("included", "Included"),
    ]

    TRANSFER_CHOICES = [
        ("group", "Group"),
        ("private", "Private"),
    ]

    CURRENCY_CHOICES = [
        ("AMD", "AMD"),
        ("USD", "USD"),
        ("EUR", "EUR"),
    ]
    
    title = models.CharField(max_length=150)

    start_date = models.DateField()
    end_date = models.DateField()

    meal_plan = models.CharField(max_length=20,choices=MEAL_CHOICES)
    transfer_type = models.CharField(max_length=20,choices=TRANSFER_CHOICES)
    hotel_name = models.CharField(max_length=150)
    hotel_type = models.CharField(max_length=50)
    ticket_included = models.BooleanField(default=False)
    baggage_included = models.BooleanField(default=False)

    latitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
    longitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    adults = models.PositiveIntegerField(default=1)
    children_under_2 = models.PositiveIntegerField(default=0)
    children_2_12 = models.PositiveIntegerField(default=0)
    children_12_plus = models.PositiveIntegerField(default=0)

    price = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(Decimal("0.01"))])
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES,default="AMD")
    airline_name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title