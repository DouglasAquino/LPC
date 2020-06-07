from django.contrib import admin
from .models import Pessoa, PessoaFisica, Evento, Ingresso, Inscricao

admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(Ingresso)
admin.site.register(Inscricao)
