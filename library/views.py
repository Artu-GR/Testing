from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Client, Lending
from .forms import BookForm, ClientForm, LendingForm
from django.contrib import messages


# Agregar un libro
def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list') #regresa a la pagina princial
        else:
            messages.error(request, "Error al agregar el libro. Verifica los campos.")
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
        form = BookForm(request.POST, request.FILES ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            messages.error(request, "Error al agregar el libro. Verifica los campos.")
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book.html', {'form': form, 'book': book})

#elimina un libro
def book_delete(request,pk):
    book= get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


# Agregar un cliente/usuario
def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list') #regresa a la pagina princial
        else:
            messages.error(request, "Error al agregar el cliente. Verifica los campos.")
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
            messages.error(request, "Error al agregar el cliente. Verifica los campos.")
            
    else:
        form = ClientForm(instance=client)
    return render(request, 'library/client.html', {'form': form, 'client': client})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')

#Agregar un prestamo
def lending(request):
    books = Book.objects.all()
    clients = Client.objects.all()
    print("Clientes:", clients)
    if request.method == 'POST':
        form = LendingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lending_list') #regresa a la pagina princial
        else:
            messages.error(request, "Error al agregar el préstamo. Verifica los campos.")
    else:
        form = LendingForm()
    return render(request, 'library/lending.html', {'form': form,'books':books, 'clients':clients})

def lending_list(request):
    lendings = Lending.objects.all()
    return render(request,'library/lending_list.html',{'lendings':lendings})

def lending_edit(request, pk):
    books = Book.objects.all()
    clients = Client.objects.all()
    lending = get_object_or_404(Lending, pk=pk)
    if request.method == 'POST':
        form = LendingForm(request.POST, instance=lending)
        if form.is_valid():
            form.save()
            return redirect('lending_list')
        else:
            print(form.errors)
            messages.error(request, "Error al agregar el préstamo. Verifica los campos.")
            
    else:
        form = LendingForm(instance=lending)
    return render(request, 'library/lending.html', {'form': form, 'lending': lending,'books':books, 'clients':clients})

def lending_delete(request, pk):
    lending = get_object_or_404(Lending, pk=pk)
    lending.delete()
    return redirect('lending_list')