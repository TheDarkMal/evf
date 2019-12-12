from django.contrib import admin
from .models import Evento, espacios, EspacioOtro,servicios

# Register your models here.

admin.site.register(Evento)
admin.site.register(espacios)
admin.site.register(EspacioOtro)
admin.site.register(servicios)
