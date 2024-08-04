from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model, get_user
from django.views import View
from .models import User
from login.forms import RegisterForm, LoginAccountForm
from django.utils.crypto import get_random_string

# user = get_user_model()

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        login_form = LoginAccountForm()
        return render(
            request,
            'login/login.html',
            {'register_form': register_form, 'login_form': login_form}
        )


    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            UM = register_form.cleaned_data.get('email')
            UP = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=UM).exists()
            if user:
                register_form.add_error('email', 'ایمیل قبلا توسط کاربر دیگری ثبت شده')
            else:
                new_user = User(
                    email=UM,
                    A_email=get_random_string(72),
                    is_active=False,
                    username=register_form.name
                )
                new_user.set_password(UP)
                new_user.save()
                # todo: send email active code
                return redirect(reversed('profile'))

        login_form = LoginAccountForm(request.POST)
        if login_form.is_valid():
            print(login_form.cleaned_data)
        context = {'register_form': register_form, 'login_form': login_form}
        return render(request, 'login/login.html', context)



# def login(request):
#     if request == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             return render(request, 'login/login.html', {})
#         login(request, user)
#         return redirect('home')
#     return render(request, 'login/login.html', {})
#
#
# def signup():
#     pass
#
#
#
# def Logout():
#     logout(request)
#     return redirect('home')




