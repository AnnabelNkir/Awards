from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Projects,Comment
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'project']
        fields = ['comment']



rating_choices = [ 
    (1, '1'), 
    (2, '2'), 
    (3, '3'), 
    (4, '4'), 
    (5, '5'), 
    (6, '6'), 
    (7, '7'), 
    (8, '8'),
    (9, '9'), 
    (10, '10'),
]

class Votes(forms.Form):
    design = forms.CharField(label='Design level', widget=forms.RadioSelect(choices=rating_choices))

    usability = forms.CharField(label='Usability level', widget=forms.RadioSelect(choices=rating_choices))

    creativity  = forms.CharField(label='Creativity level', widget=forms.RadioSelect(choices=rating_choices))

    content = forms.CharField(label='Content level', widget=forms.RadioSelect(choices=rating_choices))