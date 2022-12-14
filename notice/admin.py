from django.contrib import admin
from .models import Notice
from .models import Category

# Register your models here.
admin.site.register(Notice)
admin.site.register(Category)