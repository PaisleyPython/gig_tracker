from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic, View
from .models import Choice, Question, ConfirmedGigs, Vote, User, NameTag
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


# @login_required(login_url="/")
# def updateGig(request):
#     form = ConfirmedGigsForm()

#     if request.method == 'POST':
#         form = ConfirmedGigsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/calendar/')

#     context = {'form': form}
#     return render(request, 'polls/gig-form.html', context)


# =================================================================


@login_required(login_url="/")
def createPoll(request, *args, **kwargs):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/polls/')

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

@login_required(login_url="/")
def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    if Vote.objects.filter(poll_id=question_id, user_id=request.user.id).exists():
        return render(request, "polls/detail.html",
                      {"question": question, "error_message": "You have already voted on this poll"})

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
        gig_id = Vote.objects.create(poll_id=question_id,
                                     user_id=request.user.id, choice=selected_choice)

        if str(selected_choice) == "Y":
            current_user = NameTag.objects.create(name=request.user)
            match_core_members(question_id, current_user)

        createGigCard(question_id)

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# ===============================================================


def createGigCard(question_id):
    """Craetes the display card for gigs on the calendar view."""
    question = get_object_or_404(Question, pk=question_id)

    if ConfirmedGigs.objects.filter(
            request=question, venue="TBC", fee="TBC", set_type="TBC", additional_info="PENDING AVAILABILITY CONFIRMATION").exists():
        pass
    else:
        ConfirmedGigs.objects.create(
            request=question, venue="TBC", fee="TBC", set_type="TBC", additional_info="PENDING AVAILABILITY CONFIRMATION")


# ===============================================================

def match_core_members(question_id, current_user):
    question = get_object_or_404(Question, pk=question_id)

    gig = ConfirmedGigs.objects.get(request=question)
    gig.tags.add(current_user)

    # TODO This works but unfortunately it's changing all cards to confirmed.

    core_members = ["Simon", "Blod", "John", "Arwel", "Will"]
    core_members.sort()
    print(f"Core list: {core_members}")

    qs = gig.tags.all()
    qs_list = list()
    for name in qs:
        qs_list.append(str(name))
        qs_list.sort()
    print(f"qs list: {qs_list}")
    if qs_list == core_members:
        print("WE HAVE MATCHED CORE MEMBERS")
        # ConfirmedGigs.objects.filter(confirmed=None).update(confirmed=True)
        gig.confirmed = True
        gig.save()

        # gig.filter(confirmed=None).update(confirmed=True)
