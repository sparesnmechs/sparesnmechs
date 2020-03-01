# Generated by Django 3.0.3 on 2020-03-05 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carowners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpareDealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='spareparts/')),
            ],
        ),
        migrations.CreateModel(
            name='SparePartCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='spareparts/category')),
            ],
        ),
        migrations.CreateModel(
            name='SparePartSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='sparedealers.SparePartCategory')),
            ],
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('condition', models.CharField(choices=[('NEW', 'New'), ('LOCALLY USED', 'Locally Used'), ('FOREIGN USED', 'Foreign Used')], max_length=255)),
                ('year_of_manufacture', models.CharField(max_length=225)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='spareparts/')),
                ('is_featured', models.BooleanField(default=False)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carowners.CarMake')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carowners.CarModel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sparedealers.SparePartCategory')),
                ('sparedealer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sparedealers.SpareDealer')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sparedealers.SparePartSubCategory')),
            ],
        ),
    ]
