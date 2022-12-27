from django.contrib import admin
from .models import Fanart, BaseImage, FanartImage
# Register your models here.

admin.site.register(Fanart)
admin.site.register(BaseImage)
admin.site.register(FanartImage)
