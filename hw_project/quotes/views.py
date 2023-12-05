from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AuthorForm, QuoteForm, TagForm
from .models import Author, Quote, Tag
# Create your views here.
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


@login_required
def add_quote(request):
    form = QuoteForm(instance=Quote())
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
    return render(request, 'quotes/add_quote.html',
                  context={'title': 'Quotes to Scrape', 'form': form})


@login_required
def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
    return render(request, 'quotes/add_author.html',
                  context={'title': 'Quotes to Scrape', 'form': form})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "quotes/author.html", {"author": author})