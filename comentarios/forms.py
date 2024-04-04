# CRIAR O ARQUIVO forms.py 
# CÓDIGO DO FORM
from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
