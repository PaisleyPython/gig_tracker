from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name="polls"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
