from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('chat/', views.chat, name='chat'),
    path('videos/', views.videos, name='videos'),
    path('imagess/', views.members, name='images'),
    path('maps/', views.members, name='maps'),
    path('news/', views.members, name='news'),
    path(members)
]