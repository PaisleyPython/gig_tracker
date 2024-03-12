from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

# ==================================================================


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('polls')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('polls')
        else:
            messages.error(request, 'Username OR Password is incorrect')

    return render(request, 'home/home.html')

# ==================================================================


def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')

# ==================================================================


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'polls/index.html', context)
