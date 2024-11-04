from django import forms
from .models import Book, Client, Lending 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pub_date', 'autor', 'genre', 'description','availability', 'editorial','isbn']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'email']

class LendingForm(forms.ModelForm):
    class Meta:
        model = Lending
        fields = ['book', 'client', 'return_date', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset=Book.objects.all()
        self.fields['book'].label_from_instance = lambda obj:obj.title

        self.fields['client'].queryset = Client.objects.all()
        self.fields['client'].label_from_instance =lambda obj: f"{obj.name}{obj.last_name}"