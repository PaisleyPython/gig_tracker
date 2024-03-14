from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic, View
from .models import Choice, Question, ConfirmedGigs, Vote, User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ConfirmedGigsForm, QuestionForm
from django.contrib.auth.decorators import login_required
from polls.utils import get_user
from django.db.models import F

# =================================================================


def home(request):
    return render(request, 'home/home.html')

# =================================================================


@login_required(login_url="/")
def calendar(request):
    calendar = ConfirmedGigs.objects.all()
    votes = Choice.objects.all()
    context = {'calendar': calendar, 'votes': votes}
    return render(request, 'polls/calendar.html', context)


# =================================================================


@login_required(login_url="/")
def createGig(request):
    form = ConfirmedGigsForm()

    if request.method == 'POST':
        form = ConfirmedGigsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calendar/')

    context = {'form': form}
    return render(request, 'polls/gig-form.html', context)


# =================================================================


@login_required(login_url="/")
def createPoll(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')

    context = {'form': form}
    return render(request, 'polls/poll-form.html', context)


# =================================================================


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()


# =================================================================


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


# =================================================================


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# =================================================================

# @login_required(login_url="/")
# def vote(request, question_id):
#     question = get_object_or_404(Choice, pk=question_id)

#     if Vote.objects.filter(poll_id=question_id, user_id=request.user.id).exists():
#         return render(request, "polls/detail.html", {"question": question, "error_message": "You have already voted on this poll"})
#     else:
# #         question.votes += 1
#         question.save()
#         Vote.objects.create(voter=request.user, choice=question)
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# @login_required(login_url="/")
# def vote(request, question_id):

#     question = get_object_or_404(Question, pk=question_id)

#     if Vote.objects.filter(poll_id=question_id, user_id=request.user.id).exists():
#         return render(request, "polls/detail.html", {"question": question, "error_message": "You have already voted on this poll"})


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if Vote.objects.filter(poll_id=question_id, user_id=request.user.id).exists():
        return render(request, "polls/detail.html", {"question": question, "error_message": "You have already voted on this poll"})

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):

        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        Vote.objects.create(poll_id=question_id,
                            user_id=request.user.id, choice=selected_choice)
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

    #
    #
    #
    #
    #
    #
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
# =================================================================


# class PollView(View):
# class PollView(generic.DetailView):

#     def get_poll_results(self, poll):
#         poll_results = []
#         for choice in poll.choices.all():
#             voteCount = Vote.objects.filter(poll=poll, choice=choice).count()
#             poll_results.append([choice.name, voteCount])
#         return poll_results

#     def get(self, request, poll_id):
#         poll = Question.objects.get(id=poll_id)
#         poll_results = self.get_poll_results(poll)
#         return render(
#             request,
#             template_name="polls/detail.html",
#             context={
#                 "user": get_user(request),
#                 "poll": poll,
#                 "poll_results": poll_results,
#             }
#         )

#     def post(self, request, poll_id):

#         user = get_user(request)
#         if user is None:
#             return HttpResponse("Please login to continue")

#         requestData = request.POST

#         choice_id = requestData.get('choice_id')

#         poll = Question.objects.get(id=poll_id)
#         choice = Choice.objects.get(id=choice_id)
#         Vote.objects.update_or_create(
#             poll=poll,
#             user=user,
#             defaults={
#                 "choice": choice,
#             }
#         )

#         poll_results = self.get_poll_results(poll)

#         return render(
#             request,
#             template_name="polls/detail.html",
#             context={
#                 "poll": poll,
#                 "success_message": "Voted Successfully",
#                 "poll_results": poll_results,
#             }
#         )
