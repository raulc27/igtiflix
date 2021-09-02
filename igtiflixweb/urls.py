
from django.contrib import admin
from django.urls import path, include

from .views import redirect_root

urlpatterns = [
    path('',redirect_root),
    #path(route='',view=include('principal.urls')),
    path('admin/', admin.site.urls),
    path(route='principal/', view=include('principal.urls')),
    path(route='genero/',view=include('genero.urls')),
    path(route='serie/', view=include('serie.urls')),
]
