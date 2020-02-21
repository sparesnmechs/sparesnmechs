# Generated by Django 2.2.10 on 2020-02-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carowners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmake',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='spareparts/car_make'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='spareparts/car_model'),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='spareparts/'),
        ),
    ]
