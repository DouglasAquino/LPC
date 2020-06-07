from django import forms
from .models import Funcionario, Solicitacao, Atendimento, Veiculo
from datetime import date


class SolicitacaoForm(forms.Form):
    origem  = forms.CharField()
    destino  = forms.CharField()
    solicitante = forms.ModelChoiceField(queryset=Funcionario.objects.all())




class AtendimentoForm(forms.Form):
    solicitacao  = forms.ModelChoiceField(queryset=Solicitacao.objects.filter(concluida=False))
    data  = forms.DateField()
    hora = forms.TimeField()
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.all())
    motorista = forms.ModelChoiceField(queryset=Funcionario.objects.filter(cargo__nome='Motorista'))
