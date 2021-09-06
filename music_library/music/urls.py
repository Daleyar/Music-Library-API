from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.Songlist.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()),
]