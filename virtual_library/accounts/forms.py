from django import forms
from accounts.models import User


class SignInForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Почта',
                'required': True,
                'autofocus': True,
                'id': 'inputUserName',
                'type': 'user'
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'required': True,
                'id': 'inputPassword',
                'type': 'password'
            }
        )
    )
    remember_me = forms.BooleanField(label='Запомнить меня', required=False)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Никнейм',
                    'required': True,
                    'autofocus': True,
                    'type': 'user',
                    'id': 'name'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Имя',
                    'required': True,
                    'autofocus': True,
                    'type': 'user',
                    'id': 'first_name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Фамилия',
                    'required': True,
                    'autofocus': True,
                    'type': 'user',
                    'id': 'last_name'
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Почта',
                    'required': True,
                    'autofocus': True,
                    'id': 'inputEmail',
                    'type': 'email'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Пароль',
                    'required': True,
                    'id': 'inputPassword',
                    'type': 'password'
                })
        }
        labels = {
           'username': '',
           'first_name': '',
           'last_name': '',
           'email': '',
           'password': ''
        }