import os
from django.http import HttpResponse
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from django.views.generic import View
from django.conf import settings


class ArticleView(APIView):

    def _is_valid(self, url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def _get_all_images(self, url):
        """
        Returns all image URLs on a single `url`
        """
        soup = bs(requests.get(url).content, "html.parser")

        urls = []
        for img in tqdm(soup.find_all("img"), "Extracting images"):
            img_url = img.attrs.get("src")
            if not img_url:
                # if img does not contain src attribute, just skip
                continue
            img_url = urljoin(url, img_url)
            try:
                pos = img_url.index("?")
                img_url = img_url[:pos]
            except ValueError:
                pass
                if self._is_valid(img_url):
                    urls.append(img_url)
            return urls

    def get(self, request):

        articles = Article.objects.all().order_by('name')

        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    def post(self, request):
        article = request.data
        serializer = ArticleSerializer(data=article)

        if article.get('link'):
            link_urls = []
            try:
                link_urls = self._get_all_images(article['link'])
            except requests.exceptions.RequestException as err:
                print(err)
            if link_urls:
                article['image'] = link_urls[0]

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


class FrontendAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(status=501)
