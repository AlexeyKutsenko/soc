import os

from django.conf import settings
from pyhunter import PyHunter
from rest_auth.registration.serializers import RegisterSerializer as BaseRegisterSerializer
from rest_framework import serializers


class RegisterSerializer(BaseRegisterSerializer):
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)

    def validate_email(self, email):
        email = super().validate_email(email)
        api_key = os.environ.get('HUNTER_KEY')
        if api_key:
            hunter = PyHunter(api_key)
            disposable = hunter.email_verifier(email).get('disposable')
            if disposable:
                raise serializers.ValidationError('Disposable email')
        return email

    def create(self, validated_data):
        super().create(validated_data)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
