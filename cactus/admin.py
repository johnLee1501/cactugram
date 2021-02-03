from django.contrib import admin

from cactus.models import CactusModel, PictureModel


@admin.register(CactusModel)
class CactusAdmin(admin.ModelAdmin):
    list_display = ('id', 'cactus_name', 'cactus_scientific_name', 'cactus_size')


@admin.register(PictureModel)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['picture_file', 'picture_date']
