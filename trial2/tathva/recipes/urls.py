from django.urls import path

from .views import RecipeAPIView

urlpatterns =[
    path('recipes',RecipeAPIView.as_view()),
    path('recipes/<str:pk>',RecipeAPIView.as_view()),
]