# Generated by Django 3.0.3 on 2020-03-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanics', '0004_speciality_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='photo',
            field=models.ImageField(blank=True, default='1', upload_to='mechanic/'),
            preserve_default=False,
        ),
    ]
