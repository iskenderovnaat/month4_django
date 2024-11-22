from django.views import generic
from . import models, forms
from django.http import HttpResponse

class BooksListView(generic.ListView):
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class BooksFormView(generic.FormView):
    template_name = 'books/books_form.html'
    form_class = forms.ParserForm


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('200 OK')
        else:
            return super(BooksFormView, self).post(request, *args, **kwargs)