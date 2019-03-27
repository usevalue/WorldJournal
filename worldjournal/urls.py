from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from wjmaps import views as mapviews
from wjtime import views as timeviews

urlpatterns = [
    path('', views.welcome),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup),
    path('maps/', mapviews.maproom),
    path('time/', timeviews.timeline),
]
