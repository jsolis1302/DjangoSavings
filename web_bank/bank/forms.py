from django import forms

class DepositForm(forms.Form):
    oneValue = forms.IntegerField(label="$1",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    twoValue = forms.IntegerField(label="$2",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    fiveValue = forms.IntegerField(label="$5",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    tenValue = forms.IntegerField(label="$10",widget=forms.NumberInput(attrs={'class':'form-control'}),initial=0,min_value=0)
    

    


    
    