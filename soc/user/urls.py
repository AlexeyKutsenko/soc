from django.urls import re_path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from user.views import RegisterView

urlpatterns = [
    re_path(r'^registration/$', RegisterView.as_view(), name='rest_register'),
    re_path(r'^token-auth/', obtain_jwt_token),
    re_path(r'^token-verify/', verify_jwt_token)
]
