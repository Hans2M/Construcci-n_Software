from django.contrib import admin
from .forms import CustomUserCreationForm
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Lugar

# Registrar el modelo Lugar
@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'direccion', 'fecha_creacion')
    search_fields = ('nombre', 'direccion')

# Opcionalmente, registrar el modelo de User si quieres visualizarlo
from django.contrib.auth.admin import UserAdmin
admin.site.register(User, UserAdmin)

