from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from cactus.models import CactusModel, PictureModel


class ListarCactus(ListView):
    model = CactusModel
    template_name = 'home.html'
    context_object_name = 'cactus'
    # ordering = ['-date_posted']
    paginate_by = 4



class RegistrarCactus(CreateView):
    model = CactusModel
    template_name = "formulario_cactus.html"
    fields = ['cactus_name', 'cactus_scientific_name', 'cactus_description', 'cactus_size', 'cactus_picture', 'cactus_date']
    success_url = reverse_lazy('cactus-listar')


class ActualizarCactus(UpdateView):
    model = CactusModel
    template_name = 'formulario_cactus.html'
    fields = ['cactus_name', 'cactus_scientific_name', 'cactus_description', 'cactus_size']
    success_url = reverse_lazy('cactus-listar')


class EliminarCactus(DeleteView):
    model = CactusModel
    success_url = reverse_lazy('cactus-listar')
    template_name = 'confirmar_eliminar_cactus.html'


class RegistrarFotoCactus(CreateView):
    model = PictureModel
    template_name = "formulario_foto_cactus.html"
    fields = ['picture_file', 'picture_cactus']
    success_url = reverse_lazy('cactus-listar')

class ListarImagenesCactus(ListView):
    model = PictureModel
    template_name = 'imagenes_cactus.html'
    context_object_name = 'pictures'
    paginate_by = 4

    def get_queryset(self):
        cactus = get_object_or_404(CactusModel, id=self.kwargs.get('pk'))
        return PictureModel.objects.filter(picture_cactus_id=cactus.id).order_by('-picture_date')


def list_post(request):
    context = {}
    cactus = CactusModel.objects.all()
    fotos = PictureModel.objects.all()
    for cactu in cactus:
        pictures = PictureModel.objects.filter(picture_cactus=cactu)
        cactu['pictures'] = pictures
    return render(request, 'home.html', {'cactus': cactus})

#
# class PictureCreate(CreateView):
#     model = PictureModel
#     template_name = 'adopcion/solicitud_form.html'
#     form_class = PictureForm
#     second_form_class = CactusForm
#     success_url = reverse_lazy('blog-home')
#
#     def get_context_data(self, **kwargs):
#         context = super(PictureCreate, self).get_context_data(**kwargs)
#         if 'form' not in context:
#             context['form'] = self.form_class(self.request.GET)
#         if 'form2' not in context:
#             context['form2'] = self.second_form_class(self.request.GET)
#         return context
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object
#         form = self.form_class(request.POST)
#         form2 = self.second_form_class(request.POST)
#         if form.is_valid() and form2.is_valid():
#             picture = form.save(commit=False)
#             picture.cactusmodel = form2.save()
#             picture.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form, form2=form2))
