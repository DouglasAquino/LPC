from django.contrib import admin
from .models import Cargo
from .models import Departamento
from .models import Funcionario
from .models import Veiculo
from .models import Solicitacao
from .models import Atendimento

@admin.register(Cargo)
@admin.register(Departamento)
@admin.register(Funcionario)
@admin.register(Veiculo)
@admin.register(Solicitacao)
@admin.register(Atendimento)

class  TransporteAdmin(admin.ModelAdmin):
    pass
# Register your models here.
