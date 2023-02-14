from django.db import models

# Create your models here.
class ImagePro(models.Model):
    title = models.IntegerField()
    imgage = models.ImageField(upload_to='image')
    