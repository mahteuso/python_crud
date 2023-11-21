from django.forms import ModelForm
from crud_app.models import Equipament

class EquipamentForm(ModelForm):
    class Meta:
        model = Equipament
        fields = [
            'equipament_name',
            'lab_name',
            'patrimony',
        ]