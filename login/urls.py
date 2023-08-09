from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login-page'),
    path('logout/', views.logout_page, name='logout-page'),
]