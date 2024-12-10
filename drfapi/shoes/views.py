from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .serializers import SneakersSerializer
from .models import Category, Sneakers

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.



# class ShoesViewSet(viewsets.ModelViewSet):
#     # queryset = Sneakers.objects.all()
#     serializer_class = SneakersSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Sneakers.objects.all()[:3]
        
#         return Sneakers.objects.filter(pk=pk)
    

#     @action(methods=["get"], detail=True)   #http://127.0.0.1:8000/api/v1/shoeslist/2/category/
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({"cats": cats.name})


class ShoesApiList(generics.ListCreateAPIView):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ShoesApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ShoesApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer

    permission_classes=(IsAdminOrReadOnly,)

# class ShoesApiCrudView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Sneakers.objects.all()
#     serializer_class = SneakersSerializer



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