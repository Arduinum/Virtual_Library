from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from library.serializers import BookListSerializer, BookDetailSerializer
from django.views.generic import ListView
from library.models import Book


class BookViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookListSerializer


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'library/book_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)
