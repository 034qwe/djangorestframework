from django.shortcuts import render
from rest_framework import generics
from .serializers import *
# Create your views here.

from .models import  Articles

class ArticlesAPIView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializers