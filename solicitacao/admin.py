from ast import Eq
from django.contrib import admin

from solicitacao.models import Kit, Equipamento, Solicitacao

admin.site.register(Kit)
admin.site.register(Equipamento)
admin.site.register(Solicitacao)
