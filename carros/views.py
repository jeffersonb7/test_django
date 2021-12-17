from django.shortcuts import render
from .models import Carro
# Create your views here.
def index(request):
    if request.method == 'POST':
        nome =request.POST['nome']
        cor =request.POST['cor']
        print('ok')
        carro = Carro.objects.create(nome=nome, cor=cor)
        carro.save()

    return render(request, 'index.html')