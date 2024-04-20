from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
def testView(request):
    return HttpResponse('Hello World')



class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() #getting all blogpost objects that exists
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs): #adding a custom delete route to this api view to delete all existing blogposts and returns response
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")
        if title: blog_posts = BlogPost.objects.filter(title_icontains=title) #getting all blogposts with matching titles 
        else: blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True) #manually serializing the blogposts using the parameters
        return Response(serializer.data, status=status.HTTP_200_OK)
        

