# Generated by Django 4.2.7 on 2023-11-28 11:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteer', '0004_timeperiod_day_timeperiod_section_of_day_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TimePeriod',
            new_name='Time',
        ),
    ]
