# Generated by Django 3.0 on 2020-02-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonuserfields',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
