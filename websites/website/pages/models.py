from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Art(models.Model):
    name = models.CharField(max_length=100)
    art = CloudinaryField('image')
    def __str__(self):
        return self.name