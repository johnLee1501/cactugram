"""cactugram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cactus.views import PostListView, RegistrarCactus, RegistrarFotoCactus, ActualizarCactus, EliminarCactus

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('cactus/listar', PostListView.as_view(), name='cactus-listar'),
                  path('cactus/crear', RegistrarCactus.as_view(), name='cactus-crear'),
                  path('cactus/<int:pk>/actualizar/', ActualizarCactus.as_view(), name='cactus-actualizar'),
                  path('cactus/<int:pk>/eliminar/', EliminarCactus.as_view(), name='cactus-eliminar'),

                  path('foto/crear', RegistrarFotoCactus.as_view(), name='subir_foto'),
                  # path('solicitud/nueva$', PictureCreate.as_view(), name='picture_crear'),
                  # path('home/', list_post, name='home')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
