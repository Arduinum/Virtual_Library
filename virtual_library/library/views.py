from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from library.serializers import BookListSerializer, BookDetailSerializer
from django.views.generic import ListView, DetailView, FormView, TemplateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from library.models import Book, Comment
from library.forms import BookForm, CommentForm


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
        search_query = self.request.GET.get('data_search')
        # если приходят поисковые данные
        if search_query:
            # ищем уникальные id книг что подходят по запросу и были опубликованы
            books_id = Book.objects.filter(
                Q(title__icontains=search_query) | Q(authors__name__icontains=search_query), 
                is_published=True
            ).values_list('id', flat=True).distinct()
            return Book.objects.filter(id__in=books_id)
        # если данных для поиска нет выведет все данные что есть
        return super().get_queryset().filter(is_published=True)
    

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(id=self.kwargs.get('pk')) 
        context['comments'] = Comment.objects.filter(book=book)
        return context


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


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = super().get_queryset()
        book = Book.objects.get(id=self.kwargs.get('pk'))
        return queryset.filter(is_published=True, book=book)


class CommentFormView(FormView):
    form_class = CommentForm
    template_name = 'library/comment_edit.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('library:page404')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(id=self.kwargs.get('pk'))
        context['comments'] = Comment.objects.filter(is_published=True, book=book)
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.text = form.cleaned_data['text']
            comment.book = Book.objects.get(id=self.kwargs.get('pk'))
            comment.is_published = True
            comment.user = self.request.user
            comment.save()
            return redirect('library:comments', pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Page404View(TemplateView):
    template_name = 'page404.html'
