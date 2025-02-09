# Generated by Django 4.2.14 on 2024-08-03 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customuser_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=122)),
                ('eventorganizer', models.CharField(max_length=122)),
                ('day', models.CharField(max_length=122)),
                ('date', models.CharField(max_length=122)),
                ('time', models.CharField(max_length=122)),
                ('about', models.TextField(max_length=1000)),
                ('file', models.FileField(upload_to='file/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
