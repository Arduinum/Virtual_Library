from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from library.serializers import BookListSerializer, BookDetailSerializer
from django.views.generic import ListView, DetailView, FormView, TemplateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from library.models import Book
from library.forms import BookForm


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
    

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/book_detail.html'


class BookFormView(FormView):
    form_class = BookForm
    template_name = 'library/book_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect('library:page404')
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.kwargs.get('pk'):
            kwargs['instance'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return kwargs

    def form_valid(self, form):
        if self.request.user.is_authenticated or self.request.user.is_superuser:
            book = form.save(commit=False)
            book.title = form.cleaned_data['title']
            book.year = form.cleaned_data['year']
            book.description = form.cleaned_data['description']
            book.cover = form.cleaned_data['cover']
            book.is_published = form.cleaned_data['is_published']
            book.save()
            book.authors.add(*form.cleaned_data['authors'])
            return redirect('library:books')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_delete.html'
    success_url = reverse_lazy('library:books')
    context_object_name = 'book'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect('library:page404')
        return super().dispatch(request, *args, **kwargs)


class Page404View(TemplateView):
    template_name = 'page404.html'
