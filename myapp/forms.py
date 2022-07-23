from django import forms
from .models import Post, Comment, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'hashtags']

class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm) :
    class Meta :
        model = Hashtag
        fields = ['name']
