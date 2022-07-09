from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Blog
from .serializers import BlogSerializer


class BlogView(APIView):
    queryset = Blog.objects.all()

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
