from django.urls import path, include
from blog.models import Post
from rest_framework import routers
from blog.views import PostViewSet, ImageViewSet, CommentViewSet

app_name = 'blog'

router = routers.DefaultRouter()
router.register('post', PostViewSet, 'post')
router.register('image', ImageViewSet, 'image')
router.register('comment', CommentViewSet, 'comment')

urlpatterns = router.urls