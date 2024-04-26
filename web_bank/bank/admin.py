from django.contrib import admin

from .models import Bank,Account,AccountMaster,AccountDetail




# Register your models here.
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(AccountMaster)
admin.site.register(AccountDetail)
