from django.urls import path
from bank import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deposit/<int:account_id>", views.deposit, name="deposit"),
    path("account/<int:account_id>", views.accountByid, name="details"),
    path("newaccount",views.addAccount,name="newaccount"),
    path("withdraw/<int:account_id>",views.withdraw,name="withdraw")
]