# Generated by Django 3.0 on 2019-12-07 06:56

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spareparts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='spareparts/')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpareDealer',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clients.Common')),
                ('spare_parts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spareparts.SparePart')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Store')),
            ],
            bases=('clients.common',),
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clients.Common')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spareparts.Speciality')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Store')),
            ],
            bases=('clients.common',),
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clients.Common')),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spareparts.CarMake')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spareparts.CarModel')),
            ],
            bases=('clients.common',),
        ),
    ]
