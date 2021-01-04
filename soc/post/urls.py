from django.urls import re_path, include
from rest_framework import routers

from post.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    re_path(r'', include(router.urls))
]
