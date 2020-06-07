from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Noticia, MensagemDeContato
from .forms import ContatoForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse

def noticia_resumo_template(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total':total})


def noticia_detalhe(request, noticia_id):
    if request.user.is_superuser:
        try:
            noticia = Noticia.objects.get(pk=noticia_id)
            return render(request, 'app_noticias/detalhe.html', {'noticia':noticia})
        except Exception:
            raise Http404('Página não encontada')
        
        return render(request, 'app_noticias/detalhe.html', {'noticia':noticia})
    
    else:
        return HttpResponse('Voce não esta autorizado. <a href="/conta/login">Faça Login </a>')

def pagina_inicial(request):
    noticias = Noticia.objects.all()
    return render(request, 'app_noticias/inicial.html', {'todas_noticias':noticias})

class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(
            nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')


class ContatoSucessoView(TemplateView):
    template_name = 'app_noticias/contato_sucesso.html'


