# Generated by Django 4.1.5 on 2023-01-26 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heal', '0012_insuranceproducts_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recives',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recives_accout', to='heal.accounts'),
        ),
        migrations.AlterField(
            model_name='recives',
            name='insurance_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recive_insure', to='heal.insuranceproducts'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
