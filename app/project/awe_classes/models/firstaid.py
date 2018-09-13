from django.db import models


class FirstAid(models.Model):
    teacher = models.TextField()
    start_date = models.DateField()
    notes = models.TextField(
        max_length= 500,
        verbose_name='data'
    )
    total_spot = models.IntegerField()

    def __str__(self):
        return f'First Aid Class {self.start_date}'
