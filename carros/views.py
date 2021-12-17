from django.shortcuts import render

from musica.models import Musica
from .models import Carro
# Create your views here.
def index(request):
    if request.method == 'POST':
        nome =request.POST['nome']
        cor =request.POST['cor']
        print('ok')
        
        nome_musica = request.POST['musica']
        m = Musica.objects.filter(nome=nome_musica)[0]
        
        carro = Carro.objects.create(nome=nome, cor=cor, musica=m)
        carro.save()



    context = {
        'carros' : Carro.objects.all()
    }

    return render(request, 'index.html', context)