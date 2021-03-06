# Generated by Django 4.0.2 on 2022-02-25 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carehub', '0011_contact_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='application_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='registration',
            name='application_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
