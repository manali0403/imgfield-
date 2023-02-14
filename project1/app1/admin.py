from django.contrib import admin
from .models import ImagePro

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ("title" ,"imgage")

admin.site.register(ImagePro,ImageAdmin)
