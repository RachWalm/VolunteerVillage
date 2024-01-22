# Generated by Django 4.2.7 on 2024-01-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerprofile',
            name='phone',
            field=models.CharField(help_text='Must be 11 digits and numerical', max_length=12),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='skilled',
            field=models.ManyToManyField(help_text='To select multiple activities hold control and click', related_name='VolunteerProfiles', to='volunteer.skillchoices', verbose_name='Activity options'),
        ),
    ]
