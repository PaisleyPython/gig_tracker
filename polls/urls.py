from django.urls import path
from . import views


app_name = "polls"

# gig info will likely need a dynamic pk

urlpatterns = [
    path("", views.home),
    path("polls/", views.IndexView.as_view(), name="index"),
    path("calendar/", views.calendar, name="calendar"),
    path("gig-info/<str:pk>/", views.gigInfo, name="gig-info"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
