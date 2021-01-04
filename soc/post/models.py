from django.db import models

from user.models import User


class Post(models.Model):
    description = models.TextField()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['post']),
            models.Index(fields=['user'])
        ]

        unique_together = [['post_id', 'user_id']]
