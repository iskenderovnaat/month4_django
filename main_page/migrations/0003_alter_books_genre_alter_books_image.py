# Generated by Django 4.2.16 on 2024-11-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_books_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[('Детектив', 'Детектив'), ('Роман', 'Роман'), ('Детские', 'Детские')], default='Детектив', max_length=100, null=True, verbose_name='Укажите жанр книги'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='books/', verbose_name='Загрузите картинку'),
        ),
    ]
