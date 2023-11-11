from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=64)
    subTitle=models.CharField(max_length=64)
    body=models.TextField(max_length=1000)
    author=models.CharField(max_length=64)
    date=models.DateField()
    image=models.ImageField(width_field=100)