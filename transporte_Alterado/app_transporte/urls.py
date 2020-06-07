from django.urls import path

from .views import todas_solicitacoes, detalhe_solicitacao, detalhe_carro, todos_carros, detalhe_funcionario, todos_funcionarios, CadastrarView, AtendimentoView
urlpatterns = [
    path('solicitacao', todas_solicitacoes, name='inicio_solicitacao'),
    path('solicitacao/<int:datalheSolicitacao_id>/', detalhe_solicitacao, name='detalhe_solicitacao'),

    path('detalhe_carro', todos_carros, name='inicio'),
    path('detalhe_carro/<int:detalheCarro_id>/', detalhe_carro, name='detalhe_carro'),

    path('detalhe_funcionario', todos_funcionarios, name='inicio'),
    path('detalhe_funcionario/<int:detalheFuncionario_id>/', detalhe_funcionario, name='detalhe_funcionario'),

    path('solicitacao/cadastrar_solicitacao', CadastrarView.as_view(), name='cadastrar_solicitacao'),

    path('solicitacao/cadastrar_atendimento', AtendimentoView.as_view(), name='cadastrar_atendimento'),

]
