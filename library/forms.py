from django import forms
from .models import Book, Client

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pub_date', 'autor', 'genre', 'description', 'editorial']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'email']