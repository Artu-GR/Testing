from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="index"),
    path('book/', views.book, name='book'),
    path('book_list/', views.book_list, name='book_list'),
    path('client/', views.client, name='client'),
    path('client_list/', views.client_list, name='client_list'),
    path("<int:book_id>/book/", views.book, name="vote"),
]