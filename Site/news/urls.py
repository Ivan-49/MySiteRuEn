from django.urls import path, include

from .views import article_detail, redirect_home, custom_404

app_name = 'news'
urlpatterns = [
    path('', redirect_home, name='home'),
    path('<str:slug>/', article_detail, name='article_detail'),
]
