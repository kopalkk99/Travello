from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.showRegistrationForm),
    path('signup/',views.signup),
    path('login/',views.showLoginPage),
    path('userlogin/',views.login),
    path('logout/',views.logout)
]
