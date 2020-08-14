from django import forms

from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # Add input fields to be displayed in template
        fields = [
            "title",
            "content",
        ]