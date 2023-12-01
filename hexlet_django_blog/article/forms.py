from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    # можно переопределять поля модели
    name = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Article
        fields = ['name', 'body']
