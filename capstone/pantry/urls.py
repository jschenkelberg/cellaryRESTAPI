from django.urls import path
from . import views

urlpatterns = [
    path('pantry/', views.PantryList.as_view()),
]
