from django.urls import path, include
from . import views


app_name = "polls"

urlpatterns = [
    path("", views.home),
    path("polls/", views.IndexView.as_view(), name="index"),
    path("calendar/", views.IndexView.as_view(), name="calendar"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
