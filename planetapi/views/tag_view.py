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
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to tags resource

        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True,)
        return Response(serializer.data)

    @action(methods=['post', 'delete'], detail=True)
    def post_tag(self, request, pk=None):
        """Managing post tags"""
        if request.method == "POST":
            post = Post.objects.get(pk=request.data["post_id"])
            tag = Tag.objects.get(pk=pk)
            try:
                post_tag = PostTag.objects.get(post=post, tag=tag)
                return Response({'message': 'Post tag already exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            except PostTag.DoesNotExist:
                post_tag = PostTag()
                post_tag.post = post
                post_tag.tag = tag
                post_tag.save()

                return Response(status=status.HTTP_201_CREATED)

        elif request.method == "DELETE":
            post = Post.objects.get(pk=request.data["post_id"])
            tag = Tag.objects.get(pk=pk)
            try:
                post_tag = PostTag.objects.get(post=post, tag=tag)
                post_tag.delete()
                return Response(None, status=status.HTTP_204_NO_CONTENT)

            except PostTag.DoesNotExist:
                return Response({'message': 'Post tag does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized tag instance
        """
        new_tag = Tag()
        new_tag.label = request.data["label"]
        new_tag.save()

        serializer = TagSerializer(new_tag, context={'request': request})

        return Response(serializer.data)
        

    def update(self, request, pk=None):
        """Handle PUT requests for a tag

        Returns:
            Response -- Empty body with 204 status code
        """
        tag = Tag.objects.get(pk=pk)
        tag.label = request.data["label"]
        tag.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single tag

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags

    Arguments:
        serializers
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')