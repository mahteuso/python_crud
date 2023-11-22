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

    return render(request, "form.html", data)

def create(request):

        form = EquipamentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')

def view(request, pk):
    
    data = {}
    data['db'] = Equipament.objects.get(pk=pk)

    return render(request, 'view.html', data)

def edit(request, pk):
    
    data = {}
    data['db'] = Equipament.objects.get(pk=pk)
    data['form'] = EquipamentForm(instance=data['db'])

    return render(request, "form.html", data)

def update(request, pk): 

    data = {}
    data['db'] = Equipament.objects.get(pk=pk)
    form = EquipamentForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):

    db = Equipament.objects.get(pk=pk)
    db.delete()
    return redirect('home')
