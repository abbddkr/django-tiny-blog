from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class PostsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'title' : request.data.get('title'),
            'short_desc' : request.data.get('short_desc'),
            'content': request.data.get('content'),
            'author': request.data.get('author')
        }

        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def getOneByIdObject(self, postID):
        try:
            return Post.objects.get(id=postID)
        except Post.DoesNotExist:
            return None

    def get(self, request, postID, *args, **kwargs):
        post = self.getOneByIdObject(postID)
        if not post:
            return Response({'response': "Object with postID doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, postID, *args, **kwargs):
        post = self.getOneByIdObject(postID)
        if not post:
            return Response({'response': "Object with postID doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, postID, *args, **kwargs):
        post = self.getOneByIdObject(postID)
        if not post:
            return Response({'response': "Object with postID doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        post.delete()
        return Response({'response': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

