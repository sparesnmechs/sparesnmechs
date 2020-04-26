# Generated by Django 3.0.3 on 2020-04-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparedealers', '0015_auto_20200419_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='photo',
            field=models.ImageField(default='pic', upload_to='spareparts/'),
            preserve_default=False,
        ),
    ]
