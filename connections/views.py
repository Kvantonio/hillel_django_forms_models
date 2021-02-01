from connections.models import Author, Book, Creator

from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def index(request):
    return HttpResponse("Hello, you in connections")


def success(request):
    return render(request, "connections/success.html")


class CreatorCreate(LoginRequiredMixin, CreateView):
    model = Creator
    fields = ['name']
    success_url = '/connections/creator/create'

    login_url = '/admin/login/'
    redirect_field_name = 'admin'


class CreatorUpdate(LoginRequiredMixin, UpdateView):
    model = Creator
    fields = ['name']
    template_name_suffix = '_update'
    success_url = '/connections/creator/success/'
    login_url = '/admin/login/'
    redirect_field_name = 'admin'


class CreatorDelete(LoginRequiredMixin, DeleteView):
    model = Creator
    # success_url = reverse_lazy('creator-delete')
    success_url = '/connections/creator/success/'
    login_url = '/admin/login/'
    redirect_field_name = 'admin'


class CreatorDetailView(DetailView):
    model = Creator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreatorListView(ListView):
    model = Creator
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BookListView(ListView):
    model = Book
    paginate_by = 100

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['title'] = self.book.title
        return context

    def get_queryset(self, **kwargs):
        self.book = get_object_or_404(Book, title=self.kwargs['title'])
        return Author.objects.filter(book_id=self.book)
