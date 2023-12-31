from django import forms

from .models import *


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"

    def clean_address(self):
        address = str(self.cleaned_data["address"])
        if len(address) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return address

    def clean_certificate_code(self):
        certificate_code = str(self.cleaned_data["certificate_code"])
        if certificate_code != certificate_code.upper():
            raise forms.ValidationError("حروف گواهینامه باید حروف بزرگ باشد.")
        return certificate_code


class PineappleForm(forms.ModelForm):
    
    class Meta :
        model = Pineapple
        fields = "__all__"
    
    def clean_price_toman(self) :
        price = self.cleaned_data['price_toman']
        if price < 1000 :
            raise forms.ValidationError("قیمت نباید کمتر از هزار تومان باشد.")
        elif price > 1000000 :
            raise forms.ValidationError("قیمت نباید از یک میلیون تومان بیشتر باشد.")
        return price
  

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


class SubscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Subscription
        fields = '__all__'
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) == 11 and phone_number.startswith('09'):
            return phone_number
        msg = "شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود."
        raise forms.ValidationError(msg)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

    def clean_text(self):
        text = str(self.cleaned_data["text"])
        if len(text) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return text
