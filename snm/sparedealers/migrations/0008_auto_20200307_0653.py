# Generated by Django 3.0.3 on 2020-03-07 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sparedealers', '0007_auto_20200307_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparepartcategory',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='sparepartsubcategory',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='sparedealers.SparePartCategory'),
            preserve_default=False,
        ),
    ]
