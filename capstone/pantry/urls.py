from django.urls import path
from . import views

urlpatterns = [
    path('pantry/', views.PantryList.as_view()),
    path('pantry/<int:pk>/', views.FoodDetails.as_view()),
]
