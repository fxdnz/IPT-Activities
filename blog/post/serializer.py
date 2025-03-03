from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(source = 'post.title', read_only = True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_title', 'comment', 'author','created_at']