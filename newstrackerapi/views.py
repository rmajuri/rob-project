from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ArticleSerializer
from .models import Article

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('name')
    serializer_class = ArticleSerializer
