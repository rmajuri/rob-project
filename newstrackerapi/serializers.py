from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'link', 'description')

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.link = validated_data.get('link', instance.link)
        instance.description = validated_data.get('description', instance.description)

        instance.save()

        return instance
