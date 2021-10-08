from django import forms
from .models import User, Book


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=True,
                             widget=forms.EmailInput(attrs={'class': 'input email', 'name': 'email','id':'email'}))
    password = forms.CharField(max_length=20, required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'input password', 'placeholder': "at least 8 characters",
                                          'name': 'password','id' : 'password'}))

    class Meta:
        model = User
        fields = ['email', 'password']


class signUp(forms.ModelForm):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'id': 'usernameSignUp', 'class': 'input', 'name': 'usernameSignUp'}))
    email = forms.EmailField(max_length=100, required=True,
                             widget=forms.EmailInput(attrs={'class': 'input email', 'name': 'emailSignUp','id':'emailSignUp'}))
    password = forms.CharField(max_length=20, required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'input password', 'placeholder': "at least 8 characters",'id' : 'passwordSignUp',
                                          'name': 'passwordSignUp'}))

    confirm = forms.CharField(max_length=20, required=True,
                              widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'confirmPasswordSignUp',
                                                                'placeholder': "at least 8 characters",
                                                                'name': 'confirmPasswordSignUp'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm']


class Addbook(forms.ModelForm):
    CATECORY = (
        ('c++', 'c++'),
        ('python', 'python'),
        ('Java', 'Java'),
        ('algorithm', 'algorithm')
    )
    AVILABLE = (
        ('YES', 'YES'),
        ('NO', 'NO')
    )
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': "form-control"}))
    author = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': "form-control"}))
    img = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    des = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))


    class Meta:
        model = Book
        fields = ['name', 'author', 'img', 'des', 'category', 'avilable']

class editProfile(forms.ModelForm):

    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(max_length=20, required=True,
                               widget=forms.TextInput(attrs={'class': "form-control"}))

    confirm = forms.CharField(max_length=20, required=True,
                              widget=forms.TextInput(attrs={'class': "form-control"}))



    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm']
