from django.shortcuts import render
from rest_framework import generics ,viewsets
from .serializers import *
from rest_framework.views import Response
from django.forms import model_to_dict
from rest_framework.views import APIView

from .models import  Articles

# class ArticlesApiList(generics.ListCreateAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer



# class ArticlesAPIUpdate(generics.UpdateAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer


# class ArticlesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
    # queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

    def get_queryset(self):
        return Articles.objects.all()

