from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm


from . import forms

# Login view
def login_page(request):
    context = {'loginForm': forms.LoginForm()}

    if request.method == "POST":
        print(request.POST)
        login_form = forms.LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/home')

    return render(request, 'login.html', context=context)
    #return HttpResponse('<h1>Login</h1>')

# Logout_page that redirects to login page
def logout_page(request):
    logout(request)
    return redirect('/login')


"""
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('posts')
        
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('posts')
        
        # either form not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})
 """ 

    