from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'password1', 'password2']