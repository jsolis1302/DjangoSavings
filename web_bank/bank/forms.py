from django import forms

class DepositForm(forms.Form):
    oneValue = forms.IntegerField(label="$1",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    twoValue = forms.IntegerField(label="$2",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    fiveValue = forms.IntegerField(label="$5",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    tenValue = forms.IntegerField(label="$10",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)

class AccountForm(forms.Form):
    nameValue = forms.CharField(label="Account Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    amountValue = forms.IntegerField(label="Initial amount",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    withdraw = forms.BooleanField(label="Allows withdraw?",required=False)

class WithdrawForm(forms.Form):
    
    amountValue = forms.IntegerField(label="Initial amount",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    
    

    


    
    