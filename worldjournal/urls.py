from django.contrib import admin
from django.urls import path, include
from . import views
from wjmaps import views as mapviews
from wjtime import views as timeviews

urlpatterns = [
    path('', views.welcome),
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('maps/', mapviews.maproom),
    path('time/', timeviews.timeline),
]
