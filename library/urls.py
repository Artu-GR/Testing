from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="index"),
    path('book/', views.book, name='book'),
    path('book_list/', views.book_list, name='book_list'),
    path('book_edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('book_delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('client/', views.client, name='client'),
    path('client_list/', views.client_list, name='client_list'),
    path('client_edit/<int:pk>/', views.client_edit, name='client_edit'),
    path("<int:book_id>/book/", views.book, name="vote"),
    path('client_delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('lending/',views.lending, name='lending'),
    path('lending_list/',views.lending_list,name='lending_list'),
    path('lending_edit/<int:pk>/', views.lending_edit, name='lending_edit'),
    path('lending_delete/<int:pk>/', views.lending_delete, name='lending_delete'),


]