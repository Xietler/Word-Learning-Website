from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User,words,books

admin.site.register(User)
admin.site.register(words)
admin.site.register(books)