from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=55, label='Имя')
    last_name = forms.CharField(max_length=55, label='Фамилия')
    patronymic = forms.CharField(max_length=55, label='Отчество')
    username = forms.CharField(max_length=55, label='Логин')
    rules = forms.BooleanField(required=True, label='Согласие с правилами регистрации')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'patronymic', 'username', 'email', 'password1', 'password2', 'rules']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=True)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.patronymic = self.cleaned_data['patronymic']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.rules = self.cleaned_data['rules']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
