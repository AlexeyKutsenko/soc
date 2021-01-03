from django.db import models

from user.models import User


class Post(models.Model):
    description = models.TextField()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    unique_together = [['post', 'user']]

    class Meta:
        indexes = [
            models.Index(fields=['post']),
            models.Index(fields=['user'])
        ]
