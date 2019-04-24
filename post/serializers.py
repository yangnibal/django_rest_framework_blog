from django.forms import widgets
from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('url', 'title', 'passage', 'linenos', 'owner')