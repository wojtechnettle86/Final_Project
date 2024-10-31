from django.urls import path
from .views import *
from .forms import UserLoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', core, name='core'),
    path('about/', about, name="about"),
    path('profile/', profile, name="profile"),
    # path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"), 
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('registration/', registration, name="registration"),
    path('privacy_policy/', privacy_policy, name="privacy_policy"),
    path('login/',auth_views.LoginView.as_view(template_name="login.html",authentication_form=UserLoginForm),name='login'),
]