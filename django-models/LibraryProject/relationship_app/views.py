from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: Lists all books with titles and authors
def list_books(request):
    books = Book.objects.select_related('author').all()  # Efficient query with prefetch
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Details for a specific library, listing its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Prefetch books to avoid N+1 queries
        context['books'] = self.object.books.select_related('author').all()
        return context