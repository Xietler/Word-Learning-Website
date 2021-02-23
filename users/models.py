from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    statement = models.CharField(max_length=50, blank=True)
    LogoUrl = models.CharField(max_length = 200,blank = True)
    class Meta(AbstractUser.Meta):
        pass

class books(models.Model):
    user_id = models.IntegerField()
    word_id = models.IntegerField()
    note = models.TextField(blank=True)
    familiar = models.IntegerField()

class words(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.TextField(blank = True)
    phonetic = models.TextField(blank=True)
    definition = models.TextField(blank=True)
    translation = models.TextField(blank=True)
    cet4 = models.IntegerField(blank=True)
    cet6 = models.IntegerField(blank=True)
    gk = models.IntegerField(blank=True)
    gre = models.IntegerField(blank=True)
    ielts = models.IntegerField(blank=True)
    ky = models.IntegerField(blank=True)
    toefl = models.IntegerField(blank=True)
    zk = models.IntegerField(blank=True)

