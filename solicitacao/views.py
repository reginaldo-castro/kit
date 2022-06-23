from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from solicitacao.models import Kit, Solicitacao
from solicitacao.forms import SolicitacaoForm
from django.core.paginator import Paginator

from qr_code.qrcode.utils import MeCard, VCard, EpcData, WifiConfig, Coordinates, QRCodeOptions

def home_view(request):
    name = "Bem vindo"

    obj = Kit.objects.all()
    vcard_contact = VCard(
        name='',
        url='http://192.168.147.99:8000/solicitacao/solicitar/',
            )

    context = {
        'name': name,
        'vcard_contact': vcard_contact,
        'obj' : obj,
    }

    return render(request, 'solicitacao/home.html', context)



def solicitar(request):
    
    form = SolicitacaoForm()
    obj = Kit.objects.all()

    if request.method == "POST":
        form = SolicitacaoForm(request.POST, request.FILES)
        
        if form.is_valid():
            print(form)
            solicita = form.save(commit=False)
            solicita.data = timezone.now()
            solicita.hora = timezone.localtime(timezone.now())
            obj.status = "EM_USO"
            solicita.save()
            messages.success(request, "Solicitacao realizado com sucesso")
            
            return redirect('/solicitacao/listar')

    context = {
        "nome_pagina": 'Cadastrar Solicitacao',
        'form': form,
        'obj':obj
    }

    return render(request, 'solicitacao/solicitar.html', context)


def listar(request):
    solicitacao = Solicitacao.objects.all().order_by('-data')
    paginacao = Paginator(solicitacao, 10)
    numero_pagina = request.GET.get('page')
    
    try:
        pag_solicita = paginacao.get_page(numero_pagina)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        pag_solicita = paginacao.page(1)
    except EmptyPage:
        # if page is empty then return last page
        pag_solicita = paginacao.page(paginacao.num_pages)

    context = {
        "nome_pagina": 'Cadastrar Solicitacao',
        'solicitacao': solicitacao,
        "pag_solicita": pag_solicita
    }

    return render(request, 'solicitacao/listar.html', context)


def informacoes(request, id):

    solicitacao = get_object_or_404(Solicitacao, id = id)

    form = SolicitacaoForm(instance=solicitacao)

    context = {
        "nome_pagina": "Infomações do solicitacao",
        "solicitacao": solicitacao,
        "form": form,
    }

    return render(request, "solicitacao/informacoes.html", context)


def finalizar(request, id):

    if request.method == "POST":

        solicitacao = get_object_or_404(Solicitacao, id=id)
        solicitacao.status = "FINALIZADO"
        solicitacao.kit.status = "DISPONIVEL"
        solicitacao.hora_termino = timezone.localtime(timezone.now())

        solicitacao.save()

        messages.success(
            request,
            "solicitacao finalizada com sucesso"
        )

        return redirect("/solicitacao/listar")

    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )