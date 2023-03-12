
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', ArticlesAPIView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticlesAPIView.as_view(), name='article_detail'),
]