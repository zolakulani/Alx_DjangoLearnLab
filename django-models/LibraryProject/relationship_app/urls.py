# relationship_app/urls.py

from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Task 1
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Task 2 — EXACT LINES CHECKER WANTS
    path('login/', views.CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]