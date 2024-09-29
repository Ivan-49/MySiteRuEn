from django.urls import path, include
from .views import article_detail

app_name = 'news'
urlpatterns = [
    path('<slug:slug>/', article_detail, name='article_detail'),
]
