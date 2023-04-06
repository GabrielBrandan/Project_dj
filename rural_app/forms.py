from django.forms import ModelForm, TimeInput
from .models import Colectivos



class ColectivosForms(ModelForm):
    class Meta:
        model = Colectivos
        fields = ['origen', 'destino', 'hora_salida', 'hora_llegada', 'dias_de_circulacion', 'compania', 'precio']
        widgets = {
            'hora_salida': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_llegada': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
        labels = {
            'origen': 'Origen:',
            'destino': 'Destino:',
            'hora_salida': 'Hora de Salida:',
            'hora_llegada': 'Hora de Llegada:',
            'dias_de_circulacion': 'Días de Circulación:',
            'compania': 'Compañía:',
            'precio': 'Precio:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})