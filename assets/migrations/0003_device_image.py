# Generated by Django 4.2.5 on 2023-09-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_device_employee_deviceassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='device_images'),
        ),
    ]
