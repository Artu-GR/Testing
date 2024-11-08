from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField("date published", null=True, blank=True)
    autor = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    availability = models.PositiveIntegerField(default=0)
    editorial = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to="books",null=True, blank=True)

class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class Lending(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lending_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, default='out')

    