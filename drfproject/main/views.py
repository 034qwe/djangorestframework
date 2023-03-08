from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.views import Response
from django.forms import model_to_dict
# Create your views here.

from .models import  Articles



class ArticlesAPIView(generics.ListAPIView):
    def get(self,request):
        lst = Articles.objects.all().values()
        return Response({'posts':list(lst)})


    def post(self,request):
        new_post = Articles.objects.create(
            title  = request.data['title'],
            anons  = request.data['anons'],
            main_text = request.data['main_text'],
            categ_id = request.data['categ_id']
        )

        return Response({'post': model_to_dict(new_post)})


# class ArticlesAPIView(generics.ListAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializers