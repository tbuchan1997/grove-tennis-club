from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name') # These are the extra fields in addition to password
        # The UserCreationForm ALREADY includes 'password' and 'password2' fields.