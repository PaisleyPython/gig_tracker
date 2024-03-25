from django.urls import path
from . import views


app_name = "polls"

urlpatterns = [
    path("", views.home, name="home"),
    path("polls/", views.IndexView.as_view(), name="index"),
    path("calendar/", views.calendar, name="calendar"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    path("<int:question_id>/vote/", views.vote, name="vote"),

    path("create-gig/", views.createGig, name="create-gig"),

    path("create-poll/", views.createPoll, name="create-poll"),
]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
