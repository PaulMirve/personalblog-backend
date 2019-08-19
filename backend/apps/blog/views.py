from django.shortcuts import render
from rest_framework import viewsets, permissions, response, status
from blog.serializers import PostSerializer, ImageSerializer, CommentSerializer
from blog.models import Post, Image, Comment
from blog.permissions import IsGetOrIsAuthenticated


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        #permissions.IsAuthenticatedOrReadOnly  #Permission for unauthorized GET requests
        IsGetOrIsAuthenticated   # Custom permission for unauthorized GET requests
    ]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, *args, **kwargs):
         serializer = self.get_serializer(self.get_object())
         super().destroy(*args, **kwargs)
         return response.Response(serializer.data['post_id'], status=status.HTTP_200_OK)

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ImageSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save();
        return response.Response({
            'success': 1,
            'file':{
                'url': serializer.data['image_url']
            }
        }, status=status.HTTP_200_OK)

    def destroy(self, *args, **kwargs):
         serializer = self.get_serializer(self.get_object())
         super().destroy(*args, **kwargs)
         return response.Response(serializer.data['image_id'], status=status.HTTP_200_OK)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data['comment_id'], status=status.HTTP_200_OK)
