from django.urls import path

from .views import noticia_resumo_template, noticia_detalhe, pagina_inicial

urlpatterns = [
    path('resumo', noticia_resumo_template, name='resumo'),
    path('detalhe/<int:noticia_id>/', noticia_detalhe, name='detalhe'),
    path('', pagina_inicial, name='inicio')

]
