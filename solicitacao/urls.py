from django.urls import path
from solicitacao.views import home_view


urlpatterns = [
    #path('my_view/', my_view, name="qr_code"),
    path('home/', home_view),
    #path('listar/', listar),
]
