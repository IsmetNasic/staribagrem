from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    #Leave as empty string for base url
    path('', views.index, name="index"),
    path('about/', views.galerija, name="about"),
    path('meni/', views.jelovnik, name="meni"),
]