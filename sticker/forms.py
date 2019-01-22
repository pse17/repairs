'''sticker app form'''
from django.forms import ModelForm
from sticker.models import Sticker

class StickerForm(ModelForm):
    ''' Form to manipulate sticker model data'''
    class Meta:
        model = Sticker
        fields = ['court', 'device_name', 'invent_number',\
            'serial_number', 'production_date', 'malfunction']
        labels = {'invent_number': 'Инвентарный №', 'serial_number': 'Серийный № :',\
             'production_date': 'Год выпуска :', 'malfunction': 'Неисправность :'}
