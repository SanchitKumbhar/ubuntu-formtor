# Generated by Django 4.2.14 on 2024-08-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_eventinformation_fileurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinformation',
            name='fileurl',
            field=models.CharField(max_length=122),
        ),
    ]
