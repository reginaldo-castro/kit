from django.shortcuts import render
from solicitacao.models import Kit

def home_view(request):
    name = "Welcome to"

    obj = Kit.objects.get(id=1)

    context = {
        'name': name,
        'obj' : obj,
    }

    return render(request, 'solicitacao/home.html', context)




