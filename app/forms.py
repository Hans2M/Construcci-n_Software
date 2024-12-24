from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Lugar

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Campo adicional

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'descripcion', 'direccion', 'latitud', 'longitud', 'url_mapa',]