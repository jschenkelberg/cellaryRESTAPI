from django.urls import path
from . import views

urlpatterns = [
    path('pantry/', views.SongList.as_view()),
]