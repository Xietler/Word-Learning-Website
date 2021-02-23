# Generated by Django 2.0.6 on 2018-06-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_words',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('word', models.TextField(blank=True)),
                ('phonetic', models.TextField(blank=True)),
                ('definition', models.TextField(blank=True)),
                ('translation', models.TextField(blank=True)),
                ('cet4', models.IntegerField(blank=True)),
                ('cet6', models.IntegerField(blank=True)),
                ('gk', models.IntegerField(blank=True)),
                ('gre', models.IntegerField(blank=True)),
                ('ielts', models.IntegerField(blank=True)),
                ('ky', models.IntegerField(blank=True)),
                ('toefl', models.IntegerField(blank=True)),
                ('zk', models.IntegerField(blank=True)),
            ],
        ),
    ]
