# Generated by Django 2.0.6 on 2018-06-30 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180630_1744'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='word_book',
            new_name='books',
        ),
    ]
