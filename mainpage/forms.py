from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

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
    country_code = forms.CharField(max_length=5, required=True, initial='+47')

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'username', 'first_name', 'last_name', 'password1', 'password2',
                  'address', 'city', 'state_province', 'zip_postal_code', 'country', 'country_code')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        pattern = re.compile(r'^\+?[\d\s()-]*$')
        if not pattern.match(phone_number):
            raise ValidationError("Invalid phone number format.")
        return phone_number

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.search(r'^[a-zA-Z0-9._]+$', username):
            raise ValidationError("Username can only contain letters, numbers, dots, and underscores.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.search(r'^[a-zA-Z\s]+$', first_name):
            raise ValidationError("First name can only contain letters and whitespaces.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.search(r'^[a-zA-Z\s]+$', last_name):
            raise ValidationError("Last name can only contain letters and whitespaces.")
        return last_name

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not re.search(r'^[a-zA-Z0-9\s,\#\.\-\/\(\)]+$', address):
            raise ValidationError("Address can only contain letters, numbers, whitespaces, commas, periods, hyphens, slashes, parentheses, and hashes.")
        return address

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not re.search(r'^[a-zA-Z\s]+$', city):
            raise ValidationError("City can only contain letters and whitespaces.")
        return city

    def clean_state_province(self):
        state_province = self.cleaned_data.get('state_province')
        if not re.search(r'^[a-zA-Z\s]+$', state_province):
            raise ValidationError("State/Province can only contain letters and whitespaces.")
        return state_province

    def clean_zip_postal_code(self):
        zip_postal_code = self.cleaned_data.get('zip_postal_code')
        if not re.search(r'^[\d\w\s-]+$', zip_postal_code):
            raise ValidationError("Postal/ZIP Code can only contain letters, numbers, whitespaces, and hyphens.")
        return zip_postal_code

    def clean_country(self):
        country = self.cleaned_data.get('country')
        if not re.search(r'^[a-zA-Z\s]+$', country):
            raise ValidationError("Country can only contain letters and whitespaces.")
        return country

    def clean_country_code(self):
        country_code = self.cleaned_data.get('country_code')
        if not re.search(r'^\+\d{1,4}$', country_code):
            raise ValidationError("Invalid country code format.")
        return country_code