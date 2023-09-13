from django import forms
from django.core.exceptions import ValidationError

from .models import *

class SellerForm:
    
    name = forms.CharField(max_length=256)
    address = forms.CharField(widget=forms.Textarea)
    certificate_code = forms.CharField(max_length=10)

    def clean_address(self):
        address = str(self.cleaned_data["address"])
        if len(address) < 10:
            raise ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")

    def clean_certificate_code(self):
        certificate_code = str(self.cleaned_data["certificate_code"])
        if certificate_code != certificate_code.upper():
            raise ValidationError("حروف گواهینامه باید حروف بزرگ باشد.")


class PineappleForm:
    #TODO
    pass


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_weight_kg(self):
        weight_kg = self.cleaned_data['weight_kg']
        if weight_kg > 100:
            msg = '۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟'
            raise forms.ValidationError(msg)
        return weight_kg


class SubscriptionForm:
    #TODO
    pass

class CommentForm:
    #TODO
    pass
