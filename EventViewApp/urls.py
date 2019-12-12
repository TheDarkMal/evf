from django.urls import path
from .views import (cargar_inicio, EventoList, EventoCreate, LoginView, LogoutView, EventoDelete, NosotrosList)
from .views import (agregarList,espacioss,serviciosS,RegistroUsuarios,NuevoEspacioo,NuevoServicio)


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', cargar_inicio.as_view(), name = 'inicio'),
    path('eventos/', EventoList.as_view(), name = 'lista_eventos'),
    path('evento/nuevo/', EventoCreate.as_view(), name = 'nuevo_evento'),
    path('iniciasesion/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logoutsesion/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registrar/', RegistroUsuarios.as_view(), name = 'RegistroUsuarios'),
    path('agregar/', agregarList.as_view(), name = 'agregar'),
    path('nosotros/', NosotrosList.as_view(), name = 'nosotros'),
    path('espacio/', espacioss.as_view(), name = 'espacios'),
    path('espacio/nuevo/', NuevoEspacioo.as_view(), name = 'Nuevo_Espacios'),
    path('servicios/', serviciosS.as_view(), name = 'servicios'),
    path('servicios/nuevo/', NuevoServicio.as_view(), name = 'Nuevo_Servicio'),

    path('evento/delete/<int:pk>', EventoDelete.as_view(), name = 'delete_evento'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)