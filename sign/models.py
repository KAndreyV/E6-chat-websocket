from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from chat.models import Writer


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    username = forms.CharField(label="Username")

    class Meta:
        model = Writer
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

    def __str__(self):
        return f'{self.username}: {self.email}'


