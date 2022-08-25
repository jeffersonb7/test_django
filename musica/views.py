from django.shortcuts import render

from carros.views import index
from .models import Musica
from .forms import MusicaForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        musica = MusicaForm(request.POST, request.FILES)
        print(musica.is_valid())
        print(musica.errors)
        if musica.is_valid():
            musica.save()

    const = {'mus': Musica.objects.all()}

    return render(request, 'musica.html', const)