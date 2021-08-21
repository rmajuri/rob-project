from .serializers import ArticleSerializer
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ArticleView(APIView):

    def get(self, request):

        articles = Article.objects.all().order_by('name')

        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    def post(self, request):
        article = request.data
        serializer = ArticleSerializer(data=article)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response(status=204)

