from django.shortcuts import render
from rest_framework import generics ,viewsets
from .serializers import *
from rest_framework.views import Response
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsOwnerOrReadOnly


from .models import  Articles

class ArticlesApiList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class ArticlesAPIUpdate(generics.UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ArticlesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Articles.objects.all() 
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,)
# class ArticlesViewSet(viewsets.ModelViewSet):
#     # queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer

#     def get_queryset(self):
#         return Articles.objects.all()

