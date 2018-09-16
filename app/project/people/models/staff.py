from django.db import models


class Staff(models.Model):
    ADMIN = 'AD'
    TEACHER = 'TE'
    ASSISTANT = 'AS'
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (TEACHER, 'teacher'),
        (ASSISTANT, 'assistant')
    )
    PERMIT_CHOICES = (
        ('CH', 'Swiss Passport'),
        ('C', 'C-Permit'),
        ('B', 'B-Permit'),
        ('Other', 'Other'),
        ('None', 'None')
    )
    role = models.CharField(
        verbose_name='role',
        choices=ROLE_CHOICES,
        default=TEACHER,
        max_length=50,
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
    email = models.EmailField(
        verbose_name='email',
    )
    address = models.ForeignKey(
        verbose_name='address',
        to='people.Address',
        on_delete=models.CASCADE,
    )
    phone = models.TextField(
        verbose_name='phone number',
        max_length=12,
        blank=True,
        null=True
    )
    mobile = models.CharField(
        verbose_name='mobile number',
        max_length=12,
        blank=True,
        null=True
    )
    contract = models.BooleanField(
        default=False,
        verbose_name='contract'
    )
    old_ahv = models.CharField(
        max_length=14,
        verbose_name='old AHV Number',
        blank=True,
        null=True
    )
    ahv = models.CharField(
        max_length=16,
        verbose_name='AHV Number'
    )
    profession = models.CharField(
        verbose_name='profession',
        max_length=100
    )
    date_hired = models.DateField(
        blank=True,
        null=True
    )
    date_left = models.DateField(
        blank=True,
        null=True
    )
    start_salary = models.IntegerField()
    first_aid = models.ForeignKey(
        to='awe_classes.FirstAid',
        verbose_name='first aid class',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    salary_raise_date = models.DateField(
        blank=True,
        null=True
    )
    raise_step = models.IntegerField(
        blank=True,
        null=True
    )
    new_salary = models.IntegerField(
        blank=True,
        null=True
    )
    key_riehen = models.BooleanField(
        verbose_name='Has key for Riehen?',
        default=False
    )
    key_therwil = models.BooleanField(
        verbose_name='Has key for Therwil?',
        default=False
    )
    swiss_permit = models.CharField(
        choices=PERMIT_CHOICES,
        max_length=5
    )

    def __str__(self):
        return f'{self.first_name}, {self.role}'
