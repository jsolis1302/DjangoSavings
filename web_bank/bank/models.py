from django.db import models

# Create your models here.

class Bank(models.Model):

    id = models.AutoField(primary_key=True)
    total = models.FloatField()

    def __str__(self):
        return f"id: {self.id}, total: {self.total}"
    

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"id: {self.id}, amount: {self.amount}, date: {self.date}"
