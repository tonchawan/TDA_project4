# Generated by Django 4.1.5 on 2023-02-07 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heal', '0014_alter_accounts_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recives',
            name='recive_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
