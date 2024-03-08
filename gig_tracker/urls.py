from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("polls.urls")),
    path("polls/", include("polls.urls")),
    path("users/", include("users.urls")),

]
