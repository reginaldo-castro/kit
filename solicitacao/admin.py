from ast import Eq
from django.contrib import admin

from solicitacao.models import Kit, Equipamento, Solicitacao

admin.site.register(Kit)
admin.site.register(Equipamento)
@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_per_page = 5
