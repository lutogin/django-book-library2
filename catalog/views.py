from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.http import Http404


def index(req):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        req,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors
        },
    )


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        return Book.objects.all()[:5]

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book


def book_detail_view(req, pk):
    try:
        book_id = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        req,
        'book_detail.html',
        context={'book': book_id, }
    )
