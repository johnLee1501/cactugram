from django import forms

from cactus.models import CactusModel, PictureModel


class CactusForm(forms.ModelForm):
    class Meta:
        model = CactusModel
        fields = [
            'cactus_name',
            'cactus_scientific_name',
            'cactus_description',
            'cactus_size',
        ]
        labels = {
            'cactus_name': 'Nombre',
            'cactus_scientific_name': 'Nombre Científico',
            'cactus_description': 'Descripción',
            'cactus_size': 'Tamaño',
        }
        # widgets = {
        #     'cactus_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'cactus_scientific_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'cactus_size': forms.TextInput(attrs={'class': 'form-control'}),
        #     'cactus_description': forms.Textarea(attrs={'class': 'form-control'}),
        # }


class PictureForm(forms.ModelForm):
    class Meta:
        model = PictureModel
        fields = [
            'picture_file',
        ]
        labels = {
            'picture_file': 'Fotografía Cactus',

        }
        widgets = {
            'picture_file': forms.FileInput(attrs={'class': 'form-control'}),
        }
