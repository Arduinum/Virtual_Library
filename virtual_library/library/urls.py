from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, BookListView


app_name = 'library'
router = DefaultRouter()
router.register('api-books', BookViewSet, basename='api-books')

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('', include(router.urls))
]
