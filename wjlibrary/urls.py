from django.urls import path
from wjlibrary import views

urlpatterns = [
    path('', views.shelves),
    path('read/<int:world_id>', views.read),
    path('delete/<int:world_id>', views.delete),
    path('draft/', views.draft),
]

