from django import forms
from .models import Writer


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['first_name', 'last_name', 'email', 'avatar']
        exclude = ['user_id']