from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  # Only include the 'comment' field
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
        labels = {
            'comment': 'Comments'  # Change the label here
        }

class CommentDeleteForm(forms.Form):
    confirm = forms.BooleanField(widget=forms.HiddenInput(), initial=True)