# Generated by Django 3.0 on 2020-01-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='year_of_manufacture',
            field=models.DateField(),
        ),
    ]
