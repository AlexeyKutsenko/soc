from rest_framework import serializers
from rest_framework.fields import CharField, SerializerMethodField

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    description = CharField(max_length=150)
    likes = SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post
        fields = ('id', 'description', 'likes')
