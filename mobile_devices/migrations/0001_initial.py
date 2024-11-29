# Generated by Django 4.2.16 on 2024-11-29 14:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Smartphones', 'Smartphones'), ('Tablets', 'Tablets'), ('Laptops', 'Laptops')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('price', models.FloatField(verbose_name='Price')),
                ('date_of_purchase', models.DateField(verbose_name='Date of Purchase')),
                ('image', models.ImageField(upload_to='device_images/')),
            ],
            options={
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Leave a review for the device')),
                ('mark', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rate the device from 1 to 5')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='mobile_devices.device')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='tags',
            field=models.ManyToManyField(to='mobile_devices.tag', verbose_name='Tags'),
        ),
    ]
