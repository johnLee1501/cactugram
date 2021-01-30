import uuid

from django.db import models


class PictureModel(models.Model):
    picture_file = models.ImageField(upload_to='pictures', unique=True)
    picture_date = models.DateField(auto_now_add=True)


class CactusModel(models.Model):
    SIZE_CHOICES = [('S', 'Pequeño'), ('M', 'Mediano'), ('L', 'Grande')]
    cactus_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cactus_name = models.CharField(max_length=50)
    cactus_scientific_name = models.CharField(max_length=50, null=True, blank=True)
    cactus_description = models.TextField(max_length=200, null=True, blank=True)
    cactus_picture = models.ForeignKey(PictureModel, on_delete=models.CASCADE)
    cactus_size = models.CharField(max_length=1, choices=SIZE_CHOICES, blank=False)

    class Meta:
        db_table = 'cactus'

    def __str__(self):
        return self.cactus_name
