# Generated by Django 4.2.14 on 2025-01-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_formdata_detect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='detect',
        ),
        migrations.AddField(
            model_name='forminfo',
            name='detect',
            field=models.BooleanField(default=False),
        ),
    ]
