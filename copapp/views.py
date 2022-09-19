from django.shortcuts import render
from .forms import ContatoForms, PesquisaForm
from django.contrib import messages
from .models import TabelaModel

def index(request):

    times = TabelaModel.objects.all()
    mens = PesquisaForm(request.POST or None)
    game = {'time1': 'error'}
    if str(request.method) == 'POST':
        if mens.is_valid():
            data = mens.cleaned_data['pesq']
            lista = [v.time1 for c, v in enumerate(times)]
            lista2 = [v.time2 for c, v in enumerate(times)]
            if data.upper() not in lista and data.upper() not in lista2:
                messages.error(request, 'OPS!! Talvez esse time não esteja na Copa ou esteja '
                                        'escrito diferente no Banco de Dados, tente novamente.')
            else:
                for c, v in enumerate(times):
                    if data.upper() in v.time1 or data.upper() in v.time2:
                        game = {'horario': v.horario.hour,
                                'dia': v.horario.day,
                                'time1': v.time1,
                                'time2': v.time2
                                }

    mens = PesquisaForm()

    context = {
        'error': 'error',
        'resu': game,
        'pesq': mens
    }

    return render(request, 'index.html', context)


def contato(request):

    dados = ContatoForms(request.POST or None)
    if str(request.method) == 'POST':
        if dados.is_valid():
            dados.send_mail()
            messages.success(request, 'Obrigado por me contatar :)')
        else:
            messages.error(request, 'OPS!! Algo deu errado :/')
    dados = ContatoForms()

    context = {
        'formulario': dados
    }
    return render(request, 'contato.html', context)



def chaves(request):
    return render(request, 'chaves.html')