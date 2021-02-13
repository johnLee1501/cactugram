from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from cactus.models import CactusModel, PictureModel


class ListarCactus(ListView):
    model = CactusModel
    template_name = 'home.html'
    context_object_name = 'cactus'
    ordering = ['-cactus_date']
    paginate_by = 3


class RegistrarCactus(CreateView):
    model = CactusModel
    template_name = "formulario_cactus.html"
    fields = ['cactus_name', 'cactus_scientific_name', 'cactus_description', 'cactus_size', 'cactus_picture',
              'cactus_date']
    success_url = reverse_lazy('cactus-listar')


class ActualizarCactus(UpdateView):
    model = CactusModel
    template_name = 'formulario_cactus.html'
    fields = ['cactus_name', 'cactus_scientific_name', 'cactus_description', 'cactus_size', 'cactus_picture',
              'cactus_date']
    success_url = reverse_lazy('cactus-listar')


class EliminarCactus(DeleteView):
    model = CactusModel
    success_url = reverse_lazy('cactus-listar')
    template_name = 'confirmar_eliminar_cactus.html'


class ListarImagenesCactus(ListView):
    model = PictureModel
    template_name = 'galeria_cactus.html'
    context_object_name = 'pictures'
    paginate_by = 9

    def get_queryset(self):
        cactus = get_object_or_404(CactusModel, id=self.kwargs.get('pk'))
        return PictureModel.objects.filter(picture_cactus_id=cactus.id).order_by('-picture_date')


class RegistrarFotoCactus(CreateView):
    model = PictureModel
    template_name = "formulario_foto_cactus.html"
    fields = ['picture_file', 'picture_cactus']
    success_url = reverse_lazy('cactus-listar')


class ActualizarFotoCactus(UpdateView):
    model = PictureModel
    template_name = "formulario_foto_cactus.html"
    fields = ['picture_file', 'picture_cactus']
    success_url = reverse_lazy('cactus-listar')


class EliminarFotoCactus(DeleteView):
    model = PictureModel
    success_url = reverse_lazy('cactus-listar')
    template_name = 'confirmar_eliminar_cactus.html'
