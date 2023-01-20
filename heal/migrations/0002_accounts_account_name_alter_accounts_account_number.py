# Generated by Django 4.1.5 on 2023-01-20 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='account_name',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounts',
            name='account_number',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
