from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from user.forms import RegistrationForm, LoginForm
from user.models import Users

def registration_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'user/registration.html', {'form': form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/registration.html', {'form': form})

        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        age = form.cleaned_data.get('age')
        bio = form.cleaned_data.get('bio')
        avatar = form.cleaned_data.get('avatar')

        Users.objects.create_user(username=username,
                                 email=email,
                                 password=password,
                                 first_name=first_name,
                                 last_name=last_name,
                                 age=age,
                                 bio=bio,
                                 avatar=avatar
                                 )

        return redirect('main_page')

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', {'form': form})

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            form.add_error(None, 'User not founded')
            return render(request, 'user/login.html', {'form': form})

        login(request, user)

        return redirect('main_page')


def logout_view(request):
    logout(request)
    return redirect('main_page')

@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'user/profile.html')
