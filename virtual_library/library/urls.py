from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, BookListView, BookDetailView, BookFormView, \
    Page404View, BookDeleteView, CommentListView, CommentFormView


app_name = 'library'
router = DefaultRouter()
router.register('api-books', BookViewSet, basename='api-books')

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book'),
    path('books/new/', BookFormView.as_view(), name='new_book' ),
    path('books/<int:pk>/edit/', BookFormView.as_view(), name='edit_book'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
    path('books/<int:pk>/comments/', CommentListView.as_view(), name='comments'),
    path('books/<int:pk>/comments/new/', CommentFormView.as_view(), name='new_comment'),
    path('page404/', Page404View.as_view(), name='page404'),
    path('', include(router.urls))
]
