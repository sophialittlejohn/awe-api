from django.db import models


class Classroom(models.Model):
    TH = 'Therwil'
    RH = 'Riehen'
    LOCATION_CHOICES = (
        ('Therwil', 'Therwil'),
        ('Riehen', 'Riehen')
    )
    name = models.CharField(
        max_length=50,
        verbose_name='classroom',
        blank=False
    )
    location = models.CharField(
        choices=LOCATION_CHOICES,
        max_length=7,
        verbose_name='location',
        blank=False
    )
    spots = models.IntegerField(
        verbose_name='Spots',
        blank=False
    )

    def __str__(self):
        return self.name
