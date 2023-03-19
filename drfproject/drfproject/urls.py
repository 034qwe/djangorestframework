
from django.contrib import admin
from django.urls import path , include,re_path
from main.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView


# router = routers.SimpleRouter()
# router.register('articles', ArticlesViewSet ,basename='articles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/<int:pk>/',ArticlesAPIUpdate.as_view()),
    path('api/v1/articlesdelete/<int:pk>/', ArticlesAPIDestroy.as_view()),
    path('api/v1/articles/',ArticlesApiList.as_view()),
    path('api/v1/auth/',include('djoser.urls')),
    re_path(r'^auth', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]