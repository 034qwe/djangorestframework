from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.views import Response
from django.forms import model_to_dict
from rest_framework.views import APIView

from .models import  Articles



class ArticlesAPIView(APIView):
    def get(self,request):
        w = Articles.objects.all()
        return Response({'posts':ArticlesSerializer(w,many=True).data})


    def post(self,request):
        serializer = ArticlesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_post = Articles.objects.create(
            title  = request.data['title'],
            anons  = request.data['anons'],
            main_text = request.data['main_text'],
            categ_id = request.data['categ_id']
        )

        return Response({'post': ArticlesSerializer(new_post).data})


# class ArticlesAPIView(generics.ListAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializers