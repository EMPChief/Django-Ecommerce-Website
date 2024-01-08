from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile  # Import your UserProfile model
import re

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(
        max_length=15, 
        required=True, 
        initial='+47 ',
        help_text='Enter your phone number starting with the country code.'
    )

    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        strip=False,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(),
        strip=False,
    )
    address = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    state_province = forms.CharField(max_length=100, required=True)
    zip_postal_code = forms.CharField(max_length=12, required=True)
    country = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

    def clean_general_text_field(self, field_value):
        if not re.search(r'^[\w\s.,()-]+$', field_value, re.UNICODE):
            raise ValidationError("This field contains invalid characters.")
        return field_value

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        pattern = re.compile(r'^\+\d{2}\s\d+$')
        if not pattern.match(phone_number):
            raise ValidationError("Invalid phone number format. Please use +47 12345678 format.")
        return phone_number

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.search(r'^[a-zA-Z0-9._]+$', username):
            raise ValidationError("Username can only contain letters, numbers, dots, and underscores.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_first_name(self):
        return self.clean_general_text_field(self.cleaned_data.get('first_name'))

    def clean_last_name(self):
        return self.clean_general_text_field(self.cleaned_data.get('last_name'))

    def clean_address(self):
        return self.clean_general_text_field(self.cleaned_data.get('address'))

    def clean_city(self):
        return self.clean_general_text_field(self.cleaned_data.get('city'))

    def clean_state_province(self):
        return self.clean_general_text_field(self.cleaned_data.get('state_province'))

    def clean_zip_postal_code(self):
        return self.clean_general_text_field(self.cleaned_data.get('zip_postal_code'))

    
    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address'],
                city=self.cleaned_data['city'],
                state_province=self.cleaned_data['state_province'],
                zip_postal_code=self.cleaned_data['zip_postal_code'],
                country=self.cleaned_data['country']
            )

        return user