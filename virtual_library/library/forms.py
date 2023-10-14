from django import forms
from library.models import Book, Author, Comment


class BookForm(forms.ModelForm):
    
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control mt-3',
            'placeholder': 'авторы'
        })
    )
    
    class Meta:
        model = Book
        fields = ('title', 'year', 'description', 'cover', 'is_published')
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'alt': 'cover'
                }),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control mt-3',
                    'placeholder': 'название'
                }),
            'year': forms.NumberInput(
                attrs={
                    'class': 'form-control mt-3',
                    'placeholder': 'год'
                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control mt-3',
                    'placeholder': 'описание',
                    'style': 'height: 135px'
                }),
            'is_published': forms.CheckboxInput(
                attrs={
                    'class': 'form-control mt-3 ml-1 mb-2',
                })           
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control mb-3 mt-3 border-dark',
                    'style': 'height: 140px'

                }
            )
        }
