from django.urls import path
from . import views

urlpatterns = [
    path('all_users/', views.all_users, name='all_users'),
    path('view_user/<int:id>/', views.view_user, name='view_user'),
]
