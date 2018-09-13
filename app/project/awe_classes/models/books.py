from django.db import models


class Book(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    author = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    level = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.name}, {self.author}'
