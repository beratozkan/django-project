from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("books/", views.AllBooks),
    path('', views.home, name='index'),
    path("book/<int:pk>", views.single_pool),
    path('contact/', views.contact, name='contact'),
    path('aboutUs/', views.about, name='about'),
    

]
