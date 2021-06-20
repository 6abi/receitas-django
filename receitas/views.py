from django.shortcuts import render


# Create your views here.

def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa de legumes',
        3: 'Suco verde',
        4: 'Sorvete',
        5: 'Bolo de Limão',
        6: 'Suco de abacaxi com hortelã'
    }

    dados = {
        'nome_das_receitas': receitas
    }
    return render(request,'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
