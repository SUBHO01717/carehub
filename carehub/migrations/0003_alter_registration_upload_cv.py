# Generated by Django 4.0.2 on 2022-02-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carehub', '0002_alter_registration_statement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='upload_CV',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
