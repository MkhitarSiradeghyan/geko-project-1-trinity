from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Tour


class TourModelTest(TestCase):

    def test_valid_tour(self):
        tour = Tour(
            title="Paris Tour",
            price=100
        )
        tour.full_clean() 

    def test_empty_title(self):
        tour = Tour(
            title="   ",
            price=100
        )

        with self.assertRaises(ValidationError):
            tour.full_clean()

    def test_negative_price(self):
        tour = Tour(
            title="Paris Tour",
            price=-10
        )

        with self.assertRaises(ValidationError):
            tour.full_clean()
