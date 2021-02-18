from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from cactus.models import CactusModel, PictureModel


@login_required
def search(request):
    template = 'home.html'

    query = request.GET.get('q')

    cactus = CactusModel.objects.filter(
        Q(cactus_name__icontains=query) | Q(cactus_scientific_name__icontains=query))
    paginate_by = 2
    context = {'cactus': cactus}
    return render(request, template, context)


class ListarCactus(LoginRequiredMixin, ListView):
    model = CactusModel
    template_name = 'templates/cactus/home.html'
    context_object_name = 'cactus'
    ordering = ['-cactus_date']
    paginate_by = 2


class RegistrarCactus(LoginRequiredMixin, CreateView):
    model = CactusModel
    template_name = "templates/cactus/formulario_cactus.html"
    fields = ['cactus_name', 'cactus_scientific_name', 'cactus_description', 'cactus_size', 'cactus_picture',
              'cactus_date']
    success_url = reverse_lazy('cactus-listar')


class ActualizarCactus(LoginRequiredMixin, UpdateView):
    model = CactusModel
    template_name = 'templates/cactus/formulario_cactus.html'
    fields = ['cactus_name', 'cactus_scientific_name', 'cactus_description', 'cactus_size', 'cactus_picture',
              'cactus_date']
    success_url = reverse_lazy('cactus-listar')


class EliminarCactus(LoginRequiredMixin, DeleteView):
    model = CactusModel
    success_url = reverse_lazy('cactus-listar')
    template_name = 'templates/cactus/confirmar_eliminar_cactus.html'


class ListarImagenesCactus(LoginRequiredMixin, ListView):
    model = PictureModel
    template_name = 'templates/cactus/galeria_cactus.html'
    context_object_name = 'pictures'
    paginate_by = 6

    def get_queryset(self):
        cactus = get_object_or_404(CactusModel, id=self.kwargs.get('pk'))
        return PictureModel.objects.filter(picture_cactus_id=cactus.id).order_by('-picture_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cactus'] = get_object_or_404(CactusModel, id=self.kwargs.get('pk'))
        return context


class RegistrarFotoCactus(LoginRequiredMixin, CreateView):
    model = PictureModel
    template_name = "templates/cactus/formulario_foto_cactus.html"
    fields = ['picture_file']

    def get_success_url(self):
        cactus_id = self.kwargs['pk']
        return reverse_lazy('cactus-pictures', kwargs={'pk': cactus_id})

    def form_valid(self, form):
        form.instance.picture_cactus_id = self.kwargs['pk']
        return super().form_valid(form)


class ActualizarFotoCactus(LoginRequiredMixin, UpdateView):
    model = PictureModel
    template_name = "templates/cactus/formulario_foto_cactus.html"
    fields = ['picture_file', 'picture_cactus']

    def get_success_url(self):
        cactus_id = self.kwargs['pk_cactus']
        return reverse_lazy('cactus-pictures', kwargs={'pk': cactus_id})


class EliminarFotoCactus(LoginRequiredMixin, DeleteView):
    model = PictureModel
    template_name = 'templates/cactus/confirmar_eliminar_foto.html'

    def get_success_url(self):
        cactus_id = self.kwargs['pk_cactus']
        return reverse_lazy('cactus-pictures', kwargs={'pk': cactus_id})
