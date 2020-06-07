from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'Usuário')
    nome = models.CharField('Nome', max_length=128)
    data_nascimento = models.DateField('data de Nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15, help_text='Número do telefone  no formato (99) 99999-9999', null=True, blank=True)
    telefone_fixo = models.CharField('Telefone fixo', max_length=14, help_text='Número do telefone fixo no formato (99) 9999-9999', null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    titulo = models.CharField('título', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    conteudo = models.TextField()
    titulo = models.CharField('título', max_length=128, blank=True, null=True)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True, null=True)
    data_publicacao = models.DateField('Data de publicação', max_length=128, blank=True, null=True) 
    tags = models.ManyToManyField(Tag)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentarios = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True, null=True)
    dataHora = models.DateTimeField('Horario do comentario', max_length=128, blank=True, null=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comentarios

class Foto(models.Model):
    titulo = models.CharField('título', max_length=128, blank=True, null=True)
    url = models.URLField('Foto', max_length=128, blank=True, null=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.url


class MensagemDeContato(models.Model):
    class Meta:
        verbose_name = 'Mensagem de contato'
        verbose_name_plural = 'Mensagens de contato'

    nome = models.CharField(max_length=128)
    email = models.EmailField('E-mail', null=True, blank=True)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

