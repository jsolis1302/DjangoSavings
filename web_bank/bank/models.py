from django.db import models

# Create your models here.
class Account(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=20, default="new")
        total = models.FloatField(default=0)
        withdraw = models.BooleanField(default=False)

        def __str__(self):
            return f"Account Name: {self.name}"

class AccountDetail(models.Model):
        id = models.AutoField(primary_key=True)
        amount = models.FloatField()
        date = models.DateTimeField()
        account = models.ForeignKey(Account,on_delete=models.CASCADE,default=1)

        def __str__(self):
            return f"amount: {self.amount}, date: {self.date}, account: {self.account}"
