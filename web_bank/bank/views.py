import datetime
from django import forms
from django.http import  HttpResponseRedirect, Http404
from django.shortcuts import render,redirect
from django.urls import reverse

from bank.forms import DepositForm,AccountForm,WithdrawForm

from .models import Account,AccountDetail
from django.db.models import Sum

# Create your views here.

def index(request):
    return render(request, "bank/index.html",{
        "accounts": Account.objects.all().order_by('name'),
        "total": Account.objects.aggregate(Sum('total'))['total__sum']
        #"accounts":Account.objects.all().order_by('-date')
    })

def accountByid(request,account_id):
        try:
            account = AccountDetail.objects.filter(account=account_id).order_by('-date')
            
        except AccountDetail.DoesNotExist:
            raise Http404("Detail not found.")
        return render(request, "bank/bankDetail.html", {
            "details": account,
            "account":Account.objects.get(id=account_id)
            #"passengers": flight.passengers.all(),
            #"non_passengers": Passenger.objects.exclude(flights=flight).all()
        })
    

    
def deposit(request,account_id):
    form = DepositForm()
    bank = Account.objects.get(id=account_id)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            oneval = form.cleaned_data.get('oneValue')
            twoval = form.cleaned_data.get('twoValue') *2
            fiveval = form.cleaned_data.get('fiveValue')*5
            tenval = form.cleaned_data.get('tenValue')*10

            total = oneval + twoval + fiveval + tenval
            
            newDep = AccountDetail(amount=total, date= datetime.datetime.now(),account = bank )
            newDep.save()
            accountTotal = AccountDetail.objects.filter(account=account_id).aggregate(Sum('amount'))
            newTotal = Account(id=account_id,total =accountTotal['amount__sum'],name=bank.name,withdraw = bank.withdraw)
            newTotal.save()
            return HttpResponseRedirect(reverse('details',args=(account_id,)))
    else:
        form = DepositForm()

    return render(request, "bank/deposit.html",{
        "deposit_form": form,
        "accountName":bank.name
    })

def addAccount(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            nameValue = form.cleaned_data.get('nameValue')
            amountValue = form.cleaned_data.get('amountValue')
            withdraw = form['withdraw'].value()
            print("Field withdraw",withdraw)
            newDep = Account(total=amountValue, name= nameValue, withdraw=withdraw )
            newDep.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AccountForm()

    return render(request, "bank/newAccount.html",{
        "account_form": form
    })

def withdraw(request,account_id):
    form = WithdrawForm()
    bank = Account.objects.get(id=account_id)
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amountValue = form.cleaned_data.get('amountValue')
            if amountValue <= bank.total:
                newDep = AccountDetail(amount=amountValue*-1, date= datetime.datetime.now(),account = bank )
                newDep.save()
                accountTotal = AccountDetail.objects.filter(account=account_id).aggregate(Sum('amount'))
                newTotal = Account(id=account_id,total =accountTotal['amount__sum'],name=bank.name,withdraw = bank.withdraw)
                newTotal.save()
                return HttpResponseRedirect(reverse('details',args=(account_id,)))
    else:
        form = WithdrawForm()     
    return render(request,"bank/withdraw.html",{
        "withdraw_form": form,
        "account":bank
    })