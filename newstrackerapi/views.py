import json

from django.shortcuts import render

# Create your views here.
# from rest_framework import viewsets
#
from .serializers import ArticleSerializer
# from .models import Article
#
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all().order_by('name')
#     serializer_class = ArticleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article


class ArticleView(APIView):

    def get(self, request):

        articles = Article.objects.all().order_by('name')

        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    def post(self, request):
        article = request.data

        serializer = ArticleSerializer(data=article)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        print('ARTICLE_CAT', article_saved)

        return Response(serializer.data)
