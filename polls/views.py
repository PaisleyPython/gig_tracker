from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, ConfirmedGigs
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ConfirmedGigsForm, QuestionForm


def home(request):
    return render(request, 'home/home.html')


def calendar(request):
    calendar = ConfirmedGigs.objects.all()
    votes = Choice.objects.all()
    context = {'calendar': calendar, 'votes': votes}
    return render(request, 'polls/calendar.html', context)


def createGig(request):
    form = ConfirmedGigsForm()

    if request.method == 'POST':
        form = ConfirmedGigsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calendar/')

    context = {'form': form}
    return render(request, 'polls/gig-form.html', context)


def createPoll(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')

    context = {'form': form}
    return render(request, 'polls/poll-form.html', context)


# def updateGig(request, pk):
#     gig = ConfirmedGigs.objects.get(id=pk)
#     form = ConfirmedGigsForm(instance=gig)

#     if request.method == 'POST':
#         form = ConfirmedGigsForm(request.POST, instance=gig)
#         if form.is_valid():
#             form.save()
#             return redirect('/calendar/')

#     context = {'form': form}
#     return render(request, 'polls/gig-form.html', context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
