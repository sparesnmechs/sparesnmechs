# Generated by Django 2.2.10 on 2020-02-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparedealers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='spareparts/'),
        ),
    ]
