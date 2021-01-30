from django.shortcuts import render
from django.views.generic import ListView

from cactus.models import CactusModel, PictureModel


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
    cactus = CactusModel.objects.all()
    for cactu in cactus:
        pictures = PictureModel.objects.filter(picture_cactus = cactu)
        cactu['pictures']=pictures
    return render(request, 'home.html', {'cactus': cactus})
