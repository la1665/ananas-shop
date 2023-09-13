from django import forms

from .models import *


class SellerForm:
    pass
    

class PineappleForm:
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
    pass

class CommentForm:
    pass
