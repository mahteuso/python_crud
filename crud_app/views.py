from django.shortcuts import render, redirect
from crud_app.forms import EquipamentForm
from crud_app.models import Equipament

def home(request):
    data = {}
    data['db'] = Equipament.objects.all()

    return render(request, "index.html", data)

def form(request):

    data = {}
    data['form'] = EquipamentForm()

    return render(request, "formulario.html", data)

def create(request):

        form = EquipamentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
