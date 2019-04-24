from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import permissions, renderers, viewsets
from .models import Post
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# Create your views here.

