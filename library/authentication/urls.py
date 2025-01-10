from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout')
]
