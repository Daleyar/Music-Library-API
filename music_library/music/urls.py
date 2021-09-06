from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.Songlist.as_view()),
]