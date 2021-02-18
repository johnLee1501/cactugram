import uuid
from datetime import date

from django.contrib.auth.models import User
from django.db import models


class CactusModel(models.Model):
    SIZE_CHOICES = [('S', 'Pequeño'), ('M', 'Mediano'), ('L', 'Grande')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cactus_name = models.CharField(max_length=50)
    cactus_scientific_name = models.CharField(max_length=50, null=True, blank=True)
    cactus_description = models.TextField(max_length=500, null=True, blank=True)
    cactus_size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    cactus_picture = models.ImageField(upload_to='pictures/miniatures')
    cactus_date = models.DateField(default=date.today)

    class Meta:
        db_table = 'cactus'

    def __str__(self):
        return self.cactus_name


class PictureModel(models.Model):
    picture_file = models.ImageField(upload_to='pictures', unique=True)
    picture_date = models.DateField(default=date.today)
    picture_cactus = models.ForeignKey(CactusModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture_file.name.rstrip(".jpg0123456789_png").split('/')[1]
