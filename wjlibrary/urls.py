from django.urls import path
from . import views
from .models import World

urlpatterns = [
    path('', views.shelves),
    path('read/<int:world_id>', views.desk),
    path('search/', views.shelves)
]

