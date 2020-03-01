# Generated by Django 3.0.3 on 2020-03-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='first_name',
            field=models.CharField(default='Default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speciality',
            name='last_name',
            field=models.CharField(default='User', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speciality',
            name='phone_number',
            field=models.CharField(default='07', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speciality',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='mechanic/'),
        ),
        migrations.AddField(
            model_name='speciality',
            name='store',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Mechanic',
        ),
    ]
