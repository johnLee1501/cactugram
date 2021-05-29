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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from cactus import views
from cactus.views import RegistrarCactus, RegistrarFotoCactus, ActualizarCactus, EliminarCactus, ListarCactus, \
    ListarImagenesCactus, ActualizarFotoCactus, EliminarFotoCactus
from users.views import register, profile

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('profile/', profile, name='profile'),
                  path('register/', register, name='register'),
                  path('', ListarCactus.as_view(), name='cactus-listar'),
                  path('cactus/crear', RegistrarCactus.as_view(), name='cactus-crear'),
                  path('cactus/<int:pk>/actualizar/', ActualizarCactus.as_view(), name='cactus-actualizar'),
                  path('cactus/<int:pk>/eliminar/', EliminarCactus.as_view(), name='cactus-eliminar'),
                  path('cactus/pictures/<int:pk>', ListarImagenesCactus.as_view(), name='cactus-pictures'),
                  path('foto/crear/<int:pk>', RegistrarFotoCactus.as_view(), name='subir_foto'),
                  path('foto/<int:pk>/actualizar/<int:pk_cactus>', ActualizarFotoCactus.as_view(),
                       name='foto-actualizar'),
                  path('foto/<int:pk>/eliminar/<int:pk_cactus>', EliminarFotoCactus.as_view(), name='foto-eliminar'),
                  path('search/', views.search, name='search'),
              ]
