# Generated by Django 4.2.7 on 2024-01-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0003_rename_sum_pm_timeperiod_sun_pm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeperiod',
            name='mon_am',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='mon_ev',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='mon_pm',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='wed_pm',
            field=models.BooleanField(verbose_name='Wednesday Afternoon'),
        ),
    ]