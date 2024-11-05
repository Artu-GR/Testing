from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")
    autor = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    availability = models.PositiveIntegerField(default=0)
    editorial = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to="books",null=True)

class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class Lending(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lending_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, default='out')

    