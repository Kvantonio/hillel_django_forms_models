from connections.forms import ContactForm
from connections.models import Book, Creator, Quote
from connections.tasks import contact_us

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def index(request):
    return render(request, "../templates/connections/index.html")


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


def contact_form(request):
    data = dict()
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            contact_us.delay(subject, message, from_email)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Message sent - SUCCESS')
            return redirect('connection:index')
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name='include/contact.html',
        context=context,
        request=request
    )
    return JsonResponse(data)
