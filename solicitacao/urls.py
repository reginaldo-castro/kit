from django.urls import path
from solicitacao.views import home_view, solicitar, listar, finalizar, informacoes

urlpatterns = [
    #path('my_view/', my_view, name="qr_code"),
    path('home/', home_view, name='home'),
    path('solicitar/', solicitar, name="solicitar"),
    path('listar/', listar, name="listar"),
    path('finalizar/<id>', finalizar, name="finalizar"),
    path('informacoes/<id>', informacoes, name="informacoes"),
    
]
