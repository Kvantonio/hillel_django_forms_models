from connections.models import Book, Creator, Quote

from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def index(request):
    return HttpResponse("Hello, you in connections")


def success(request):
    return render(request, "../templates/connections/success.html")


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


class QuoteListView(ListView):
    model = Quote

    def get_queryset(self, **kwargs):
        return super(QuoteListView, self).get_queryset()


class BookListView(ListView):
    model = Book
    paginate_by = 1000

    def get_queryset(self, **kwargs):
        return super(BookListView, self).get_queryset()\
            .select_related('publishing', 'description')\
            .prefetch_related('author_set')
