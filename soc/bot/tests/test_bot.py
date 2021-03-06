import json
from random import randint, choice

from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse
from rest_framework import status

from bot.tests.base import BaseTestCase
from bot.tests.factories import UserFactory, PostFactory
from post.models import Post, Like
from user.models import User


class Bot(BaseTestCase):
    number_of_users = 0
    max_posts_per_user = 0
    max_likes_per_user = 0

    def setUp(self):
        path = settings.BASE_DIR / 'bot' / 'tests' / 'config.json'
        with open(path) as config_file:
            json_config = json.load(config_file)
            self.number_of_users = json_config.get('number_of_users')
            self.max_posts_per_user = json_config.get('max_posts_per_user')
            self.max_likes_per_user = json_config.get('max_likes_per_user')

    def test_create_activity(self):
        users = []
        create_user_url = reverse('rest_register')
        for _ in range(self.number_of_users):
            user = UserFactory.build()
            response = self.client.post(create_user_url, {'email': user.email,
                                                          'password1': user.password,
                                                          'password2': user.password})
            self.assertEqual(status.HTTP_201_CREATED, response.status_code)
            user.token = response.data.get('token')
            user.username = response.data.get('user').get('username')
            users.append(user)
        self.assertEqual(User.objects.count(), self.number_of_users)

        post_url = reverse('post-list')
        for user in users:
            self.client.login(request=HttpRequest(), username=user.username, password=user.password)
            posts = [PostFactory.build() for _ in range(randint(1, self.max_posts_per_user))]
            for post in posts:
                response = self.client.post(post_url, {'description': post.description})
                self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        average_posts_per_user = Post.objects.count() / self.number_of_users
        self.assertLess(average_posts_per_user, self.max_posts_per_user)

        for user in users:
            self.client.login(request=HttpRequest(), username=user.username, password=user.password)
            posts_list = self.client.get(post_url)
            for _ in range(self.max_likes_per_user):
                post = choice(posts_list.data)
                like_url = reverse('post-like', kwargs={'pk': post['id']})
                response = self.client.post(like_url)
                self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_204_NO_CONTENT])

        average_likes_per_user = Like.objects.count() / self.number_of_users
        self.assertLess(average_likes_per_user, self.max_likes_per_user)
