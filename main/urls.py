from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('error', views.e404, name='error'),
    path('create', views.create, name='create'),
    path('login_user', views.user_login, name='login_user'),
    path('logout_user', views.user_logout, name='logout_user'),
    path('registration_user', views.user_registration, name='registration_user'),
]