from django.urls import path
from . import views

urlpatterns = [
    path('maps/', views.index, name='index'),
    path('', views.home, name='index'),
]
