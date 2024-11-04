from django.contrib import admin
from .models import Book,Client,Lending


# Register your models here.
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(Lending)