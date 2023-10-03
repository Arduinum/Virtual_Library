from django import forms
from library.models import Book, Author


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
                    'style': 'height: 160px'
                }),
            'is_published': forms.CheckboxInput(
                attrs={
                    'class': 'form-control mt-3 ml-1 mb-2',
                })           
        }
