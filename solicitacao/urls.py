from django.urls import path
from solicitacao.views import home_view, solicitar, listar


urlpatterns = [
    #path('my_view/', my_view, name="qr_code"),
    path('home/', home_view),
    path('solicitar/', solicitar),
    path('listar/', listar),
]
