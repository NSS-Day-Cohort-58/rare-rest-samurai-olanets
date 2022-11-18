from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from planetapi.models import Post
from planetapi.models import Tag
from planetapi.models import PostTag
from rest_framework.decorators import action

class TagView(ViewSet):
    """Planet view for tags"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag instance
        """
        
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag, context={'request': request})
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to tags resource

        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.all()
        post = Post.objects.get(pk=request.query_params.get('post_id', None))
        for post in posts:
            tag.post = post in 
        serializer = TagSerializer(
            tags, many=True, context={'request': request})
        return Response(serializer.data)