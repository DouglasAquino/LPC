from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.nome


class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return '{} - {}'.format(self.cpf, self.nome)


class Evento(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=10)
    descricao = models.TextField()
    data_inicio = models.DateField()
    realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Ingresso(models.Model):
    descricao = models.CharField(max_length=150)
    valor = models.FloatField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
       return self.descricao


class Inscricao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE)

    def __str__(self):
        return '{} esta inscrita no evento {}({}) com o ingresso {}'.format(self.pessoa.nome, self.evento.nome, self.evento.sigla, self.ingresso)
