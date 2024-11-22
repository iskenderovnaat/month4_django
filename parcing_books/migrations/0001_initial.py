# Generated by Django 4.2.16 on 2024-11-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=900)),
                ('image', models.ImageField(upload_to='books/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
