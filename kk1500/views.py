from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Checks if user is logged in, if not redirects to login page
@login_required(login_url='/login')
def LandingPage(request):
    return redirect('/home')



