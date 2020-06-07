from django.db import models
from django.contrib.auth.models import User


class Cargo(models.Model):
    nome = models.CharField('Nome', max_length=128, blank=True, null=True)
    sigla = models.CharField('Sigla', max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=128, blank=True, null=True)
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=128, blank=True, null=True)
    matricula = models.CharField('Matricula',max_length=10, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ['nome']
        verbose_name = 'Funcionário'

    def __str__(self):
        return "{} - {} ".format(self.nome, self.cargo.nome)


class Veiculo(models.Model):
    descricao = models.CharField('Descrição', max_length=150, blank=True, null=True)
    modelo = models.CharField('Modelo', max_length=100, blank=True, null=True)
    placa = models.CharField('Placa', max_length=10, blank=True, null=True)
    def __str__(self):
        return "{} - {} ".format(self.modelo, self.placa)


class Solicitacao(models.Model):
    origem = models.CharField('Origem', max_length=150, blank=True, null=True)
    destino = models.CharField('Destino', max_length=150, blank=True, null=True)
    data_hora = models.DateTimeField(auto_now_add=True, verbose_name='data da solicitação')
    solicitante = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)
    concluida = models.BooleanField(default=False)
    class Meta:
        ordering = ['solicitante__nome']
        verbose_name = 'solicitação'
        verbose_name_plural = 'solicitações'

    def __str__(self):
        return '{id:06d} {solicitante}'.format(id=self.id, solicitante=self.solicitante.nome)


class Atendimento(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField('Data do atendimento', max_length=128, blank=True, null=True)
    hora = models.TimeField('Hora do atendimento', max_length=128, blank=True, null=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, null=True, blank=True)
    motorista = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return '{}: {}'.format(self.motorista, self.solicitacao)
