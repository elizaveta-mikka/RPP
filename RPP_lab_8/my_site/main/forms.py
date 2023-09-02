from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
        }

