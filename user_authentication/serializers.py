#serializers take an instance of the python object and convert it into something for us to interact with from our api

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"] #fields to be returned in api
        