# Generated by Django 2.0.3 on 2018-11-17 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awe_classes', '0009_auto_20180922_1631'),
        ('people', '0011_auto_20181026_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='awe_class',
        ),
        migrations.AddField(
            model_name='student',
            name='awe_class',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='awe_classes.AWEClass', verbose_name='class'),
            preserve_default=False,
        ),
    ]
