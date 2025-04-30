from django.urls import path
from .views import RegisterView, BookListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', BookListView.as_view(), name='book_list'),
]
