import datetime
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render,redirect
from django.urls import reverse

from bank.forms import DepositForm,AccountForm

from .models import Bank,Account

# Create your views here.

def index(request):
    
    return render(request, "bank/index.html",{
        "banks": Bank.objects.all().order_by('name')
        #"accounts":Account.objects.all().order_by('-date')
    })

def allBanks(request):
    return render(request, "bank/index.html",{
        "bank": Bank.objects.first(),
        "accounts":Account.objects.all().order_by('-date')
    })

def accountByid(request,bank_id):
        try:
            account = Account.objects.filter(account=bank_id).order_by('date')
            
        except Account.DoesNotExist:
            raise Http404("Detail not found.")
        return render(request, "bank/bankDetail.html", {
            "accounts": account,
            "bank":Bank.objects.get(id=bank_id)
            #"passengers": flight.passengers.all(),
            #"non_passengers": Passenger.objects.exclude(flights=flight).all()
        })
    

    
def deposit(request,bank_id):
    form = DepositForm()
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            oneval = form.cleaned_data.get('oneValue')
            twoval = form.cleaned_data.get('twoValue') *2
            fiveval = form.cleaned_data.get('fiveValue')*5
            tenval = form.cleaned_data.get('tenValue')*10

            total = oneval + twoval + fiveval + tenval

            bank = Bank.objects.get(id=bank_id)
            updatedAmount = bank.total + total
            newdate  = datetime.datetime.now().date()
            newTotal = Bank(id=bank_id,total =updatedAmount,name=bank.name)
            newTotal.save()
            newDep = Account(amount=total, date= newdate,account = bank )
            newDep.save()
            #return redirect("account/"+str(bank_id))
            return HttpResponseRedirect(reverse('details',args=(bank_id,)))
    else:
        form = DepositForm()

    return render(request, "bank/deposit.html",{
        "deposit_form": form
    })

def addAccount(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            nameValue = form.cleaned_data.get('nameValue')
            amountValue = form.cleaned_data.get('amountValue')
            

            newDep = Bank(total=amountValue, name= nameValue )
            newDep.save()
    else:
        form = AccountForm()

    return render(request, "bank/newAccount.html",{
        "account_form": form
    })

