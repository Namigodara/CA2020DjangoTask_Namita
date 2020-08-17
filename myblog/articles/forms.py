from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # Add input fields to be displayed in template
        fields = [
            "title",
            "content",
        ]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length = 30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)