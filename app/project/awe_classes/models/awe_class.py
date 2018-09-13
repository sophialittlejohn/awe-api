from django.db import models


class AWEClass(models.Model):
    PROGRAM_CHOICES = (
        ('ESOL', 'ESOL'),
        ('EFES', 'EES'),
        ('PRES', 'Preschool'),
        ('PRIV', 'Private'),
        ('SPTH', 'Speech Therapy'),
        ('TUTR', 'Tutoring')
    )
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    )
    name = models.CharField(
        max_length=70,
        verbose_name='class name'
    )
    teacher = models.ManyToManyField(
        to='people.Staff',
        verbose_name='teacher',
        blank=False,
    )
    day = models.CharField(
        verbose_name='Day of the Week',
        max_length=10,
        choices=DAY_CHOICES
    )
    start_time = models.TimeField(
        max_length=15,
    )
    end_time = models.TimeField(
        max_length=15,
    )
    class_room = models.ForeignKey(
        to='awe_classes.Classroom',
        verbose_name='class room',
        on_delete=models.CASCADE
    )
    total_classes = models.IntegerField(
        verbose_name='total classes'
    )
    program = models.CharField(
        choices=PROGRAM_CHOICES,
        max_length=4,
        verbose_name='program'
    )
    session = models.ForeignKey(
        to='awe_classes.Session',
        on_delete=models.CASCADE,
        verbose_name='Session'
    )
    books = models.ForeignKey(
        to='awe_classes.Book',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
