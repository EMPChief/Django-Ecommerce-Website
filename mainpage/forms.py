from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    state_province = forms.CharField(max_length=100, required=True)
    zip_postal_code = forms.CharField(max_length=12, required=True)
    country = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'username', 'first_name', 'last_name', 'password1', 'password2',
                  'address', 'city', 'state_province', 'zip_postal_code', 'country')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email 