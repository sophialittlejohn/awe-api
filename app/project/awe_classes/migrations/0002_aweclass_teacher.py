# Generated by Django 2.0.3 on 2018-09-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('awe_classes', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aweclass',
            name='teacher',
            field=models.ManyToManyField(to='people.Staff', verbose_name='teacher'),
        ),
    ]
