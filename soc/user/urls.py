from django.urls import include, re_path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    re_path(r'^registration/', include('rest_auth.registration.urls')),
    re_path(r'^token-auth/', obtain_jwt_token),
    re_path(r'^token-verify/', verify_jwt_token)
]