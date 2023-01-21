# Generated by Django 4.1.5 on 2023-01-20 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heal', '0003_alter_accounts_account_number_alter_accounts_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_Identity',
            field=models.BigIntegerField(default=0, validators=[django.core.validators.RegexValidator('^\\d{14}$', 'Enter a valid 14 digit number.')]),
        ),
        migrations.AddField(
            model_name='users',
            name='user_first_name',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='users',
            name='user_last_name',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]