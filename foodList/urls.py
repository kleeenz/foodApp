from django.urls import path
from . import views

#controller for the view functions mapping each view to a pattern.
urlpatterns = [
    path('', views.allFood, name = 'allFood'),
    path('foodView/', views.foodView, name = 'foodView'),
    path('deleteFood/<int:id>/', views.deleteFood, name = 'deleteFood'),
]
