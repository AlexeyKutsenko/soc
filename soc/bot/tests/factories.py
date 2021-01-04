from factory import Faker
from factory.django import DjangoModelFactory

from user.models import User


class UserFactory(DjangoModelFactory):
    """
    Creates Account objects
    """

    class Meta:
        """
        Meta
        """
        model = User

    password = Faker('password')
    email = Faker('email')
