from django.shortcuts import render
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, LikeSerializer, ViewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category, Post, Comment, Like
from .permissions import IsAdminOrReadOnly, IsCurrentUserOwnerOrAdminOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from .paginations import MyCursorPagination
from rest_framework.filters import SearchFilter




class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsCurrentUserOwnerOrAdminOrReadOnly,)
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = MyCursorPagination
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')




