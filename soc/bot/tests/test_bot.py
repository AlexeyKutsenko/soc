import json

from django.conf import settings

from bot.tests.base import BaseTestCase


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
