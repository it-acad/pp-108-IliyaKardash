from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_authors, name='all_authors'),
    path('create/', views.create_author, name='create_author'),
    path('delete/<int:author_id>/', views.delete_author, name='delete_author'),
]
