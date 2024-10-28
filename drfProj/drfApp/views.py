from django.shortcuts import render
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework import mixins


# Create your views here.
# class BlogListAV(APIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     def get(self,request):
#         blogs=Blog.objects.all()
#         serializer=BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer=BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class BlogDetailAV(APIView):
#     def get_obj(self,pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesNotExist:
#             raise Http404

#     def get(self,request,pk):
#         blog=self.get_obj(pk)
#         serializer=BlogSerializer(blog)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         blog=self.get_obj(pk)
#         serializer=BlogSerializer(blog,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         blog=self.get_obj(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class BlogListGV(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class BlogDetailGV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
class BlogListCV(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogDetailCV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]