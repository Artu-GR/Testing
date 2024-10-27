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

class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()