# Generated by Django 4.2.14 on 2024-08-11 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_formdata_eventinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='customuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
