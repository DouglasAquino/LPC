from django import forms
from .models import Chamado, Status, Categoria


class ChamadosForm(forms.Form):
    titulo = forms.CharField(max_length=50)    
    descricao = forms.CharField(widget=forms.Textarea)
    telefone = forms.CharField(max_length=10)
    categoria = forms.CharField(max_length=10)


    def clean(self):
        dados = super().clean()
        return dados
