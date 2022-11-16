from rest_framework.viewsets import ViewSet
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from planetapi.models import Post

class PostView(ViewSet):
    def create(self, request):
        """Handle POST operations.
        Returns
        JSON serialized post instance"""
        category = Category.objects.get(pk=request.data["category"])
        post = Post.objects.create(
            title = request.data["title"],
            content = request.data["content"],
            date= request.data["date"],
            image = request.data["image"],
            # category = category
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def list(self, request):
        """Handle GET request, all posts. """
        posts=Post.objects.all()
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET request for a single post. """
        post=Post.objects.get(pk=pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """ Handle PUT request for a single post. """
        post = Post.objects.get(pk=pk)
        post.title=request.data["description"]
        post.content=request.data["content"]
        post.date=request.data["date"]
        post.image=request.data["image"]
        post.category=request.data["category"]
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts."""
    class Meta:
        model=Post
        fields=("id", "title", "content", "category", "date", "image")