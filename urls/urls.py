from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import UserViewSet
from post.views import PostViewSet
from rest_framework import routers

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include('router.urls')),
]