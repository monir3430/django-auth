from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User was successfully registered')
            return redirect('success_url')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
