from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from cactus.forms import PictureForm, CactusForm
from cactus.models import CactusModel, PictureModel


class RegistrarCactus(CreateView):
    model = CactusModel
    template_name = "formulario_cactus.html"
    fields = ['cactus_name', 'cactus_scientific_name', 'cactus_description', 'cactus_size']
    success_url = reverse_lazy('listar')


class PostListView(ListView):
    model = CactusModel
    template_name = 'home.html'
    context_object_name = 'cactus'
    ordering = ['cactus_name']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PostListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


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
