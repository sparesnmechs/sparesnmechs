# Generated by Django 3.1.7 on 2021-07-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='created_by',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='otp',
            name='updated_by',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
