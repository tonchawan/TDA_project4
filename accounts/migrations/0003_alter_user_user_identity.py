# Generated by Django 4.1.5 on 2023-01-26 13:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_user_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_Identity',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.RegexValidator('^\\d{13}$', 'Enter a valid 13 digit account number.')]),
        ),
    ]
