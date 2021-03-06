import math

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.forms import HypotenuseFrom, MyPersonModelForm, ReminderForm

from .models import Choice, MyPerson, Question
from .tasks import send_date_reminder


class IndexView(generic.ListView):
    template_name = '../templates/polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = '../templates/polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = '../templates/polls/results.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, '../templates/polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,))
            )


def hypotenuse_form(request):
    gip = None
    if request.method == "GET":
        form = HypotenuseFrom()
    else:
        form = HypotenuseFrom(request.POST)
        if form.is_valid():
            first_leg = form.cleaned_data['first_leg']
            second_leg = form.cleaned_data['second_leg']
            gip = math.sqrt(first_leg ** 2 + second_leg ** 2)
    return render(
        request,
        "../templates/polls/triangle.html",
        context={
            "form": form,
            "gip": gip
        }
    )


def reminder_form(request):
    if request.method == "GET":
        form = ReminderForm()
    else:
        form = ReminderForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            rem_date = form.cleaned_data['date']

            send_date_reminder.apply_async((email, text), eta=rem_date)

    return render(
        request,
        "../templates/polls/reminder.html",
        context={
            "form": form,
        }
    )


def auth_modelform(request):
    if request.method == "GET":
        form = MyPersonModelForm()
    else:
        form = MyPersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:person')
    return render(
        request,
        "../templates/polls/person.html",
        context={
            "form": form,
        }
    )


def output_personal_data_modelform(request, id):  # noqa: A002
    pn = get_object_or_404(MyPerson, id=id)
    if request.method == "GET":
        form = MyPersonModelForm(instance=pn)
    else:
        form = MyPersonModelForm(request.POST, instance=pn)
        if form.is_valid():
            form.save()
    return render(
        request,
        "../templates/polls/person_res.html",
        context={
            "pn": pn,
            "form": form,
        }
    )
