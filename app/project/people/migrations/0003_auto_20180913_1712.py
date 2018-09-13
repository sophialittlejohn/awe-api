# Generated by Django 2.0.3 on 2018-09-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20180913_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='ahv',
            field=models.CharField(max_length=16, verbose_name='ahv number'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='old_ahv',
            field=models.CharField(max_length=14, verbose_name='old ahv number'),
        ),
    ]