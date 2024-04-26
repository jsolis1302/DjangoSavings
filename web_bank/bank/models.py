from django.db import models

# Create your models here.

class Bank(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="new")
    total = models.FloatField()

    def __str__(self):
        return f"Account Name: {self.name}"
    

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    date = models.DateField()
    account = models.ForeignKey(Bank,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"amount: {self.amount}, date: {self.date}, account: {self.account}"
    
class AccountMaster(models.Model):
    pass

class AccountDetail(models.Model):
    pass
