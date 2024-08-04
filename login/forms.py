from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام کاربر'}),
        # label='Name'
    )
    email = forms.EmailField(
        # label='Email',
        widget=forms.EmailInput(attrs={'placeholder':'آدرس ایمیل'}),
    )
    password = forms.CharField(
        # label='Password',
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور'}),
    )
    confirm_password = forms.CharField(
        # label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور'}),
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError("کلمه عبور و تکرار کلمه عبور یکسان نیست")

class LoginAccountForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام کاربر'}),
        # label='Name'
    )
    password = forms.CharField(
        # label='Password',
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور'}),
    )


