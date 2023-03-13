from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.views import Response
from django.forms import model_to_dict
from rest_framework.views import APIView

from .models import  Articles

class ArticlesApiList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


#not work
class ArticlesAPIView(APIView):
    def get(self,request):
        w = Articles.objects.all()
        return Response({'posts':ArticlesSerializer(w,many=True).data})


    def post(self,request):
        serializer = ArticlesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({'post': serializer.data})


    def put(self,request, *args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        
        try:
            instance = Articles.objects.get(pk=pk)
        
        except:
            return Response({'error':'Object does not exists'})

        serializer = ArticlesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':serializer.data})


