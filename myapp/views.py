from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User was successfully registered')
                return redirect('success_url')
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')


def success_view(request):
    return render(request, 'success.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
                else:
                    form.add_error(None, "Invalid username or password")
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    else:
        return redirect('profile')


# if request.method == 'POST':
#     form = AuthenticationForm(request=request, data=request.POST)
#     if form.is_valid():
#         # Log in the user
#         user = form.get_user()
#         login(request, user)
#         # Redirect to home
#         return redirect('home')
# else:
#     form = AuthenticationForm()
#
# return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # update_session_auth_hash(request, form.cleaned_data['user'])
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'passchange.html', {'form': form})


def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # update_session_auth_hash(request, form.cleaned_data['user'])
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'passchange.html', {'form': form})


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account updated successfully!')
                return redirect('success_url')
        else:
            form = ChangeForm(instance=request.user)
        return render(request, 'info-change.html', {'form': form})
    else:
        return redirect('signup')
