from django.db import models


class Address(models.Model):
    # SUI = 'Switzerland'
    # GER = 'Germany'
    # FRA = 'France'
    COUNTRY_CHOICES = (
        ('SUI', 'Switzerland'),
        ('GER', 'Germany'),
        ('FRA', 'France')
    )
    street = models.CharField(
        verbose_name='street',
        max_length=100
    )
    number = models.IntegerField(
        verbose_name='house number'
    )
    city = models.CharField(
        verbose_name='city',
        max_length=70
    )
    zip = models.IntegerField(
        verbose_name='zip'
    )
    country = models.CharField(
        choices=COUNTRY_CHOICES,
        max_length=3,
        verbose_name='country'
    )

    def __str__(self):
        address = f'{self.street}, {self.number}, {self.city}'
        return address
