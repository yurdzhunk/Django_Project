from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = "Posts"
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    class Meta:
        db_table = "Comments"
    author = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField()
    post = models.ForeignKey(Post)

class Title(models.Model):
    class Meta:
        db_table = "Title"
    name = models.CharField(max_length=100)