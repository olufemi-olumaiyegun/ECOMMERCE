from django import forms
from .models import User
from django.db import models
from django.core.exceptions import ValidationError
userchoices = (("Buyer","Buyer"), ("Seller","Seller"), ("Both","Both")) #choices of type of user
#model1 = get_user_model()  # form is based on a basic django created user model


class RegisterNewUser(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)

    i_am_a = forms.ChoiceField(choices=userchoices)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exist = User.objects.filter(email=email)
        if exist.exists():
            raise ValidationError("Email is already registered with another account")
        return email
    def clean_password2(self):
        data = self.cleaned_data
        password1=self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password2 !=password1:
            raise ValidationError("Passwords do not match")
        return password1,password2
    def save(self, commit=True):
        #save password in encrypted format
        user = super(RegisterNewUser,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = True ##make sure to change this to false when working with email confirmations
        if commit:
            user.save()
        return user
    if i_am_a == 'Seller':
        User.seller = True
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'i_am_a']
