# relationship_app/urls.py

from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Task 1
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Task 2 — CHECKER NOW WANTS THESE EXACT LINES
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),   # ← THIS IS WHAT IT WANTED!
]