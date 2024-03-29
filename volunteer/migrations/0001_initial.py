# Generated by Django 4.2.7 on 2024-01-23 16:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(help_text='This is require and has a maximum length of 50 characters', max_length=50, verbose_name='First Name')),
                ('lname', models.CharField(help_text='This is require and has a maximum length of 50 characters', max_length=50, verbose_name='Last Name')),
                ('phone', models.CharField(help_text='Must be 11 digits and numerical', max_length=12)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('special_skills_description', models.TextField(blank=True, help_text='If you wish to provide us with specific information about skills - type it here', max_length=500, verbose_name='Information')),
                ('activated', models.BooleanField(default=False)),
                ('time_length_hours', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(168)], verbose_name='Hours per week you can be available')),
                ('time_length_days', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7)], verbose_name='days per week you can be available')),
                ('mon_am', models.BooleanField(default=False, verbose_name='Monday morning')),
                ('mon_pm', models.BooleanField(default=False, verbose_name='Monday afternoon')),
                ('mon_ev', models.BooleanField(default=False, verbose_name='Monday evening')),
                ('tue_am', models.BooleanField(default=False, verbose_name='Tuesday morning')),
                ('tue_pm', models.BooleanField(default=False, verbose_name='Tuesday afternoon')),
                ('tue_ev', models.BooleanField(default=False, verbose_name='Tuesday Evening')),
                ('wed_am', models.BooleanField(default=False, verbose_name='Wednesday morning')),
                ('wed_pm', models.BooleanField(default=False, verbose_name='Wednesday afternoon')),
                ('wed_ev', models.BooleanField(default=False, verbose_name='Wednesday evening')),
                ('thu_am', models.BooleanField(default=False, verbose_name='Thursday morning')),
                ('thu_pm', models.BooleanField(default=False, verbose_name='Thursday afternoon')),
                ('thu_ev', models.BooleanField(default=False, verbose_name='Thursday Evening')),
                ('fri_am', models.BooleanField(default=False, verbose_name='Friday morning')),
                ('fri_pm', models.BooleanField(default=False, verbose_name='Friday afternoon')),
                ('fri_ev', models.BooleanField(default=False, verbose_name='Friday evening')),
                ('sat_am', models.BooleanField(default=False, verbose_name='Saturday morning')),
                ('sat_pm', models.BooleanField(default=False, verbose_name='Saturday afternoon')),
                ('sat_ev', models.BooleanField(default=False, verbose_name='Saturday evening')),
                ('sun_am', models.BooleanField(default=False, verbose_name='Sunday morning')),
                ('sun_pm', models.BooleanField(default=False, verbose_name='Sunday afternoon')),
                ('sun_ev', models.BooleanField(default=False, verbose_name='Sunday evening')),
                ('skilled', models.ManyToManyField(help_text='To select multiple activities hold control and click', related_name='VolunteerProfiles', to='volunteer.skillchoices', verbose_name='Activity options')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
