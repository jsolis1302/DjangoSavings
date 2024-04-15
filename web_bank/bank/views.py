import datetime
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from bank.forms import DepositForm

from .models import Bank,Account

# Create your views here.

def index(request):
    print(Account.objects.all())
    return render(request, "bank/index.html",{
        "bank": Bank.objects.first(),
        "accounts":Account.objects.all().order_by('-date')
    })
    
def deposit(request):
    form = DepositForm()
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            oneval = form.cleaned_data.get('oneValue')
            twoval = form.cleaned_data.get('twoValue')
            fiveval = form.cleaned_data.get('fiveValue')
            tenval = form.cleaned_data.get('tenValue')

            fintwo = twoval * 2
            finfive = fiveval * 5
            finten = tenval * 10
            total = oneval + finfive + fintwo+ finten


            bank = Bank.objects.first().total
            updatedAmount = bank + total
            newdate  = datetime.datetime.now().date()
            print(newdate)
            newTotal = Bank(id=1,total =updatedAmount)
            newTotal.save()
            newDep = Account(amount=total, date= newdate )
            newDep.save()
    else:
        form = DepositForm()

    return render(request, "bank/deposit.html",{
        "deposit_form": form
    })
