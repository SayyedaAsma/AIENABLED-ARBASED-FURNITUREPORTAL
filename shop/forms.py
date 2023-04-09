from django import forms
from django.contrib.auth import get_user_model
from .models import Products,User

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

...
class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
   
class SetPasswordForm(SetPasswordForm):
    class meta:
        model = get_user_model()
        fields = ('password1', 'password2')

   

class ProductsForms(forms.ModelForm):
    p_images = forms.ImageField(required=False)
   
    class Meta:
        model = Products
        fields="__all__"