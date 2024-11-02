from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Book, Client
from .forms import BookForm, ClientForm

def index(request):
    return HttpResponse("Welcome")

# Agregar un libro
def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') #regresa a la pagina princial
    else:
        form = BookForm()
    return render(request, 'library/book.html', {'form': form})

#Lista de libros registrados
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

#Editar info de libros registrados
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book.html', {'form': form, 'book': book})


# Agregar un cliente/usuario
def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list') #regresa a la pagina princial
    else:
        form = ClientForm()
    return render(request, 'library/client.html', {'form': form})

#Lista de clientes registrados
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'library/client_list.html', {'clients': clients})

#Editar info de clientes registrados
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        else:
            print(form.errors)
    else:
        form = ClientForm(instance=client)
    return render(request, 'library/client.html', {'form': form, 'client': client})