# Generated by Django 3.0.3 on 2020-04-19 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparedealers', '0014_auto_20200418_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='description',
            field=models.TextField(default='describe'),
            preserve_default=False,
        ),
    ]
