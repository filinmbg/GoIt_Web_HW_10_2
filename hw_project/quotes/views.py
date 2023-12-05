from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from bson import ObjectId

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


def authors_by_tags(request, tag_name):
    """Перехід по тегу"""

    tags = Tag.objects.filter(name=tag_name).first()
    quotes = tags.quote_set.all()
    return render(request, "quotes/tags.html", context={"quotes": quotes})


def about(request, quote_id):
    """Перехід по кнопці 'about'"""

    description = Author.objects.filter(pk=quote_id)
    return render(request, "quotes/description.html", context={"authors": description})

class AuthorDetailView(DetailView):
    template_name = 'quotes/author_detail.html'

    def get(self, request, pk: str):
        db = get_mongodb()
        author = db.authors.find_one({'_id': ObjectId(pk)})
        print(author)
        return render(request, self.template_name, context={'author': author})

