from django.contrib.auth.models import User
from django import forms

from music.models import Song


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email','password']


class Add_Song(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['file_type', 'song_title']

class loginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']