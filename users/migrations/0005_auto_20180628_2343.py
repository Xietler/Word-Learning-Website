# Generated by Django 2.0.6 on 2018-06-28 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_words'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users_words',
            new_name='words',
        ),
    ]
