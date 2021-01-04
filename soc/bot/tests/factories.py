from factory import Faker
from factory.django import DjangoModelFactory

from post.models import Post
from user.models import User


class PostFactory(DjangoModelFactory):
    """
    Creates Post objects
    """

    class Meta:
        model = Post

    description = Faker('pystr')


class UserFactory(DjangoModelFactory):
    """
    Creates User objects
    """

    class Meta:
        model = User

    password = Faker('password')
    email = Faker('email')
