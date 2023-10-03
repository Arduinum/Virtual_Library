from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, BookListView, BookDetailView, BookFormView, \
    Page404View


app_name = 'library'
router = DefaultRouter()
router.register('api-books', BookViewSet, basename='api-books')

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book'),
    path('books/new/', BookFormView.as_view(), name='new_book' ),
    path('books/<int:pk>/edit/', BookFormView.as_view(), name='edit_book'),
    path('page404/', Page404View.as_view(), name='page404'),
    path('', include(router.urls))
]
