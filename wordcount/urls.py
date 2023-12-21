from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load_file/', views.load_file, name='load_file'),
    path('word_count/', views.word_count, name='word_count'),
    path('clear_memory/', views.clear_memory, name='clear_memory'),
]