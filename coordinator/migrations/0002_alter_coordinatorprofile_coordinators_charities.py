# Generated by Django 4.2.7 on 2024-01-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_initial'),
        ('coordinator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinatorprofile',
            name='coordinators_charities',
            field=models.ManyToManyField(to='charity.charityprofile', verbose_name='coordinators associated charities'),
        ),
    ]