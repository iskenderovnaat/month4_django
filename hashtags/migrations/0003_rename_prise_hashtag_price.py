# Generated by Django 4.2.16 on 2024-11-12 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0002_alter_hashtag_prise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='prise',
            new_name='price',
        ),
    ]