from django.urls import path
from . import views

urlpatterns = [
    
    #Home
    
    path('', views.home, name='store-home'),
    path('buy/',views.buy,name='store-buy')
]