from django.shortcuts import render
from django.views import View
from .models import Chamado, Atendimento, Funcionario, Categoria, Status
from chamados.forms import ChamadosForm
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, FormView



def inicial(request):
    chamados = []
    if request.user.is_authenticated:
        if request.user.is_superuser:
            chamados = Chamado.objects.filter()
        else:
            chamados = Chamado.objects.filter(autor__usuario=request.user)
    else:
        return render(request, 'chamados/erro_autenticacao.html', {})

    return render(request, 'chamados/inicial.html', {'chamados': chamados})


def detalhes(request, id_chamado):
    if request.user.is_authenticated:
        chamado = Chamado.objects.get(pk=id_chamado)
        return render(request, 'chamados/detalhes.html', {'chamado': chamado})
    else:
        return render(request, 'chamados/erro_autenticacao.html', {})

class ChamadoView(FormView):
    template_name = 'chamados/chamado.html'
    form_class = ChamadosForm

    
    def form_valid(self, form):
        dados = form.clean()
        cat = Categoria.objects.create()
        cat.nome = Categoria(nome=dados['categoria'])
        cat.nome.save()
 
        
        chamados = Chamado(
            titulo=dados['titulo'], descricao=dados['descricao'], telefone=dados['telefone'],
            categoria = cat)
        chamados.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('chamado_sucesso')


class ChamadoSucessoView(TemplateView):
    template_name = 'chamados/chamado_sucesso.html'

