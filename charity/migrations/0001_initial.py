# Generated by Django 4.2.7 on 2023-12-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharityProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_name', models.CharField(help_text='format: required, max_length=50', max_length=50, verbose_name='Charity Name')),
                ('charity_description', models.TextField(verbose_name='Charity Description')),
            ],
        ),
    ]
