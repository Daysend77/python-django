from django import forms
from .models import Comment, Author, Book



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('nick', 'text')
        widgets = {
            'nick': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name',)
        labels = {
            'name': 'ФИО'
        }


class BookForm(forms.ModelForm):

    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None)

    class Meta:
        model = Book
        fields = ('title', 'description', 'author')
        labels = {
            'title': 'Название',
            'description': 'Описание',
        }