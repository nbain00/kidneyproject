from django.urls import path
from .views import indexPageView, foodJournalView, addFoodView, levelsLogView, addLevelView, deleteLogView
from .views import profileEditView, foodinMealView
urlpatterns = [
    path('', indexPageView, name="index"),
    path('journal/<int:userid>/<str:date1>', foodJournalView, name="journal"),
    path('add-food/<int:userid>', addFoodView, name="add-food"),
    path('log/<int:userid>', levelsLogView, name="log"),
    path('add-level/<int:userid>', addLevelView, name="add-level"),
    path("deleteLog/<int:userid>/<int:logid>/", deleteLogView, name="deleteLog"),
    path("showProfile/<int:userid>/", profileEditView, name="showProfile"),
    path('food-in-meal/<int:userid>/<str:mealtype>/<int:logid>/<str:date1>', foodinMealView, name="food-in-meal"),
]