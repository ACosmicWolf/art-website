from django.db import models
import django.utils
import datetime
# Create your models here.
class Painting(models.Model):
    name = models.CharField(max_length=100)
    art = models.ImageField(upload_to='static/')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE,blank=True,null=True,related_name="painting")
    date = models.DateField(("Date"), default=django.utils.timezone.now)
    def __str__(self):
        return self.name

