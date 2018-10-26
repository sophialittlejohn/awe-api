from django.db import models


class Student(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=30,
    )
    birthdate = models.DateField(
        verbose_name='birthday',
    )
    gender = models.TextField(
        choices=GENDER_CHOICES,
        max_length=6,
    )
    email = models.EmailField(
        verbose_name='email',
    )
    address = models.ForeignKey(
        verbose_name='address',
        to='people.Address',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    phones = models.CharField(
        verbose_name='phone numbers',
        max_length=12,
        blank=True,
        null=True
    )
    mother_name = models.CharField(
        verbose_name='mother name',
        max_length=30,
        blank=True,
        null=True
    )
    mother_workplace = models.CharField(
        verbose_name='mother workplace',
        max_length=50,
        blank=True,
        null=True
    )
    father_name = models.CharField(
        verbose_name='father name',
        max_length=30,
        blank=True,
        null=True
    )
    father_workplace = models.CharField(
        verbose_name='father workplace',
        max_length=50,
        blank=True,
        null=True
    )
    cambridge_exam = models.CharField(
        verbose_name='cambridge exam',
        max_length=100,
        blank=True,
        null=True
    )
    registered = models.BooleanField(
        verbose_name='registered',
    )
    start_date = models.DateField(
        verbose_name='start date'
    )
    end_date = models.DateField(
        verbose_name='end date',
        blank=True,
        null=True
    )
    awe_class = models.ManyToManyField(
        verbose_name='class',
        to='awe_classes.AWEClass',
    )
    cost_per_class = models.IntegerField(
        verbose_name='cost per class',
        blank=True,
        null=True
    )
    discount = models.CharField(
        verbose_name='discount',
        blank=True,
        null=True,
        max_length=10
    )
    notes = models.TextField(
        verbose_name='notes',
        blank=True,
        null=True
    )


