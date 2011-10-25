from django import forms
from bbblog.blog.models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

