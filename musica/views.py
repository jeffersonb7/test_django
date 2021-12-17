from django.shortcuts import render

from carros.views import index

# Create your views here.
def index(request):
    return render(request, 'musica.html')