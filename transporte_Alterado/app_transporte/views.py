from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from .models import Solicitacao, Veiculo, Funcionario, Atendimento
from .forms import SolicitacaoForm, AtendimentoForm

from django.views.generic.edit import FormView

def todas_solicitacoes(request):
    todas = []
    if request.user.is_authenticated:
        funcionario = Funcionario.objects.get(usuario = request.user)
        if funcionario.cargo.nome == 'Chefe':
            todas = Solicitacao.objects.filter(solicitante__usuario=request.user)
        elif funcionario.departamento.nome == 'Transporte':
            todas = Solicitacao.objects.filter(concluida = False)
    else:
        return render(request, 'app_transporte/erro_autenticacao.html', {})
    return render(request, 'app_transporte/solicitacao.html', {'todas_solicitacao':todas,
                                                                 'funcionario':funcionario} )

def detalhe_solicitacao(request, datalheSolicitacao_id):
    if request.user.is_authenticated:
        detalhesolicitacao = Solicitacao.objects.get(pk=datalheSolicitacao_id)
        return render(request, 'app_transporte/detalhe_solicitacao.html', 
        {'detalhesolicitacao':detalhesolicitacao})
    else:
        return render(request, 'app_transporte/erro_autenticacao.html', {})
    

def todos_carros(request):
    if request.user.is_authenticated:
        todos = Veiculo.objects.all()
        return render(request, 'app_transporte/veiculo.html', {'todo_carro':todos})
    else:
        return render(request, 'app_transporte/erro_autenticacao.html', {})
    

def detalhe_carro(request, detalheCarro_id):
    if request.user.is_authenticated:
        detalhecarro = Veiculo.objects.get(pk=detalheCarro_id)
        return render(request, 'app_transporte/detalhe_carro.html', {'detalhecarro':detalhecarro})
    else:
        return render(request, 'app_transporte/erro_autenticacao.html', {})
    
def todos_funcionarios(request):
    if request.user.is_authenticated:
        todos = Funcionario.objects.all()
        return render(request, 'app_transporte/funcionario.html', {'todo_funcionario':todos})
    else:
        return render(request, 'app_transporte/erro_autenticacao.html', {})
    

def detalhe_funcionario(request, detalheFuncionario_id):
    if request.user.is_authenticated:
        detalhefuncionario = Funcionario.objects.get(pk=detalheFuncionario_id)
        return render(request, 'app_transporte/detalhe_funcionario.html', {'detalhefuncionario':detalhefuncionario})
    else:
        return render(request, 'app_transporte/erro_autenticacao.html', {})
    


class CadastrarView(FormView):
    template_name = "app_transporte/cadastrar_solicitacao.html"
    form_class = SolicitacaoForm
    def form_valid(self, form):
        dados = form.clean()
        autor=Funcionario.objects.get(usuario=self.request.user)
        mensagem = Solicitacao(origem=dados['origem'], destino=dados['destino'],
                           solicitante=autor)
        mensagem.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('inicio_solicitacao')


class AtendimentoView(FormView):
    template_name = "app_transporte/cadastrar_atendimento.html"
    form_class = AtendimentoForm
    def form_valid(self, form):
        dados = form.clean()
        mensagem = Atendimento(solicitacao=dados['solicitacao'], data=dados['data'], hora=dados['hora'],
                           veiculo=dados['veiculo'], motorista=dados['motorista'])
        mensagem.save()
        chamado=Solicitacao.objects.get(pk=dados['solicitacao'].pk)
        chamado.concluida=True
        chamado.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('inicio_solicitacao')

