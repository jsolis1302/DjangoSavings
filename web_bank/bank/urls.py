from django.urls import path
from bank import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deposit", views.deposit, name="deposit"),
]