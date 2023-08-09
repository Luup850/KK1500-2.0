from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return render(request, 'base.html')
    return HttpResponse('<h1>Store Home</h1>')

# Create your views here.
