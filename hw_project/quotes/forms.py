from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, ModelChoiceField, \
    ModelMultipleChoiceField, Select, SelectMultiple
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = DateField(widget=DateInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(max_length=500, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class TagForm(ModelForm):
    name = CharField(max_length=25, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(ModelForm):
    quote = CharField(max_length=1000, widget=TextInput(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'),
                              widget=Select(attrs={"class": "form-select"}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'),
                                    widget=SelectMultiple(attrs={"class": "form-select", "size": "7"}))
    # tags = CharField(max_length=10, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']