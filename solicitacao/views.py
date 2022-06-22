from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from solicitacao.models import Kit, Solicitacao
from solicitacao.forms import SolicitacaoForm

def home_view(request):
    name = "Bem vindo"

    obj = Kit.objects.get(id=1)

    context = {
        'name': name,
        'obj' : obj,
    }

    return render(request, 'solicitacao/home.html', context)



def solicitar(request):
    
    form = SolicitacaoForm()
    obj = Kit.objects.get()

    if request.method == "POST":
        form = SolicitacaoForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            solicita = form.save(commit=False)
            solicita.data = timezone.now()
            solicita.hora = timezone.now()
            solicita.kit.status = "EM_USO"
            solicita.save()
            messages.success(request, "Solicitacao realizado com sucesso")
            
            return redirect('/solicitacao/listar')

    context = {
        "nome_pagina": 'Cadastrar Solicitacao',
        'form': form
    }

    return render(request, 'solicitacao/solicitar.html', context)


def listar(request):
    solicitacao = Solicitacao.objects.all()
    print(solicitacao)
    context = {
        "nome_pagina": 'Cadastrar Solicitacao',
        'solicitacao': solicitacao
    }

    return render(request, 'solicitacao/listar.html', context)