# Generated by Django 4.2.16 on 2024-11-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_books_created_at_books_stock_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]