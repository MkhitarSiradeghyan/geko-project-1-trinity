from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255, verbose_name="Վերնագիր")
    description = models.TextField(verbose_name="Նկարագրություն")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Թարմացման ամսաթիվ")

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title