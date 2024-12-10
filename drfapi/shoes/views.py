from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics

from .serializers import SneakersSerializer
from .models import Sneakers

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class ShoesApiList(generics.ListCreateAPIView):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer

class ShoesApiUpdate(generics.UpdateAPIView):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer

class ShoesApiCrudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer



# class ShoesApiView(APIView):
#     def get(self, request):
#         arr = Sneakers.objects.all()
#         return Response({'posts': SneakersSerializer(arr,many=True).data})
    
#     def post(self, request):
#         ser = SneakersSerializer(data=request.data)
#         ser.is_valid(raise_exception=True)
#         ser.save()
#         return Response({'post': ser.data})
    
#     def put(self,request, *args, **kwargs ):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': "not put"})
        
#         try:
#             instance = Sneakers.objects.get(pk=pk)
#         except:
#             return Response({'error': "not pk"})
        
#         serializer = SneakersSerializer(data=request.data, instance = instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'posts': serializer.data})
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "not delete"})
        
#         Sneakers.objects.filter(pk=pk).delete()

#         return Response({"post": "delete post" + str(pk)})



# class ShoesApiView(generics.ListAPIView):
#     queryset = Sneakers.objects.all()
#     serializer_class = SneakersSerializer