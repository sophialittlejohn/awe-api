from django.db import models


class Session(models.Model):
    name = models.CharField(
        max_length=70
    )
    start_date = models.DateField(
        blank=False
    )
    end_date = models.DateField(
        blank=False
    )
    number_of_classes = models.IntegerField(
        blank=False
    )
    notes = models.TextField(
        max_length=250,
        blank=True
    )

    def __str__(self):
        return self.name