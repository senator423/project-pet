# Generated by Django 5.0.2 on 2025-03-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_petapp', '0002_contactmessage_service_blogpost_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(max_length=100),
        ),
    ]
