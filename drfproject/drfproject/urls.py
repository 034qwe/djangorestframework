
from django.contrib import admin
from django.urls import path , include
from main.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register('articles', ArticlesViewSet ,basename='articles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls))
#     path('articles/', ArticlesViewSet.as_view({'get':'list'}), name='articles'),
#     path('articles/<int:pk>/', ArticlesViewSet.as_view({'put':'update'}), name='article_put'),
#     path('articlesdetail/<int:pk>/', ArticlesViewSet.as_view(), name='article_detail')
    ]