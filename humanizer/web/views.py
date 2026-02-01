from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, "web/index.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "web/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('index')

def ai_detector(request):
    return render(request, "web/ai_detector.html")

def humanizer(request):
    return render(request, "web/humanizer.html")

def grammar_checker(request):
    return render(request, "web/grammar_checker.html")
