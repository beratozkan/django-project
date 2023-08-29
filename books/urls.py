from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("pools/", views.pools),
    path('', views.home, name='index'),

]
