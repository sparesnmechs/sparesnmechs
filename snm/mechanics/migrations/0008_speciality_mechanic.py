# Generated by Django 3.0.3 on 2020-03-12 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mechanics', '0007_auto_20200312_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='mechanic',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
