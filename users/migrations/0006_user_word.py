# Generated by Django 2.0.6 on 2018-06-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180628_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('word_id', models.IntegerField()),
                ('note', models.TextField(blank=True)),
                ('familiar', models.IntegerField()),
            ],
        ),
    ]
