# Generated by Django 2.0.3 on 2018-09-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awe_classes', '0007_auto_20180913_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aweclass',
            name='program',
            field=models.CharField(choices=[('ESOL', 'ESOL'), ('EFES', 'EES'), ('Preschool', 'Preschool'), ('Private', 'Private'), ('Speech Therapy', 'Speech Therapy'), ('Tutoring', 'Tutoring')], max_length=4, verbose_name='program'),
        ),
    ]
