# Generated by Django 4.2.16 on 2024-11-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_alter_reviewbooks_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default='2023-01-01', verbose_name='дата создания'),
        ),
        migrations.AddField(
            model_name='books',
            name='stock_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество книг в наличии'),
        ),
    ]