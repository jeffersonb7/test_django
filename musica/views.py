from django.shortcuts import render

from carros.views import index
from .models import Musica
# Create your views here.
def index(request):
    if request.method == 'POST':
        mus = request.POST['mus']
        Musica(nome=mus).save()

    const = {'mus': Musica.objects.all()}

    return render(request, 'musica.html', const)