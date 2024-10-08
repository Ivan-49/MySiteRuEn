from django.urls import path, include

from .views import article_detail, redirect_home

app_name = 'news'
urlpatterns = [
    path('', redirect_home, name='home'),
    path('<slug:slug>/', article_detail, name='article_detail'),
]
