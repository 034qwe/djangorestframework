
from django.contrib import admin
from django.urls import path , include,re_path
from main.views import *
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register('articles', ArticlesViewSet ,basename='articles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articlesupdate/<int:pk>/',ArticlesAPIUpdate.as_view()),
    path('api/v1/drf/', include('rest_framework.urls')),
    path('api/v1/articlesdelete/<int:pk>/', ArticlesAPIDestroy.as_view()),
    path('api/v1/articles/',ArticlesApiList.as_view()),
    path('api/v1/auth/',include('djoser.urls')),
    re_path(r'^auth', include('djoser.urls.authtoken'))

    ]