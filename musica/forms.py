from django.forms import ModelForm
from .models import Musica

class MusicaForm(ModelForm):
    class Meta:
        model = Musica
        fields = ('nome', 'duracao', 'file_arquivo')
        labels = {
            'nome': 'nome',
            'duracao': 'duracao',
            'file_arquivo': 'file_arquivo'
            # 'nome': 'mus',
            # 'duracao': 'dur'
        }