# Generated by Django 4.2.7 on 2024-01-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_alter_timeperiod_mon_am_alter_timeperiod_mon_ev_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeperiod',
            name='fri_am',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='fri_ev',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='fri_pm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='mon_am',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='mon_ev',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='mon_pm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='sat_am',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='sat_ev',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='sat_pm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='sun_am',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='sun_ev',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='sun_pm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='thu_am',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='thu_ev',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='thu_pm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='tue_am',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='tue_ev',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='tue_pm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='wed_am',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='wed_ev',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='timeperiod',
            name='wed_pm',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Wednesday Afternoon'),
        ),
    ]
