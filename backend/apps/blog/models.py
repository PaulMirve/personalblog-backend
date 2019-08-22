from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey("auth.User", db_column='author', on_delete = models.CASCADE, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.ImageField(max_length=200, upload_to='media',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Post', db_column='post', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    author_email = models.CharField(max_length=50)
    author_image = models.CharField(max_length=150)
    text = models.TextField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'