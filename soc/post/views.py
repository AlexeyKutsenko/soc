from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from post.models import Post, Like
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        instance = self.get_object()

        like = instance.likes.filter(user=request.user).first()
        if like:
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            like = Like(post=instance, user=request.user)
            like.save()
            return Response(status=status.HTTP_201_CREATED)
