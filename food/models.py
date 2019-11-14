from django.db import models


class abc(models.Model):
    head = models.CharField(max_length=100)
    descr = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='clicks')
