from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import BookForm, ClientForm

def index(request):
    return HttpResponse("Welcome")

# Agregar un libro
def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('') #regresa a la pagina princial
    else:
        form = BookForm()
    return render(request, 'library/book.html', {'form': form})

# Agregar un cliente/usuario
def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('') #regresa a la pagina princial
    else:
        form = ClientForm()
    return render(request, 'library/client.html', {'form': form})