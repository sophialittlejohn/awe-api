# Generated by Django 2.0.3 on 2018-09-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awe_classes', '0003_auto_20180913_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='location',
            field=models.CharField(choices=[('Therwil', 'Therwil'), ('Riehen', 'Riehen')], max_length=2, verbose_name='location'),
        ),
    ]
