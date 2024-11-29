from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models
import datetime
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books_list'
    paginate_by = 10

    def get_queryset(self):
        return models.Books.objects.select_related().order_by('-id')

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class BooksListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books_list'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Hi! My name is Asema and I study in GEEKS. I'm 16 y.o.")


def about_my_pet(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://s0.rbk.ru/v6_top_pics/media/img/9/73/756723943137739.webp'>- This is my cat, Barni", )


def system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())