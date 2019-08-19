from rest_framework import serializers
from blog.models import Post, Image

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'title', 'text', 'created_date']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_id', 'image_url']